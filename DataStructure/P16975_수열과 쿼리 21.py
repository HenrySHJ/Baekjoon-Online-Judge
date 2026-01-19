import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
A = list(map(int,input().split()))

tree = [0]*(4*N)
lazy = [0]*(4*N)

# 세그먼트 트리 최초 작성
def build(node,start,end):
    # 세그먼트 트리 leaf node에 값 넣기
    if start == end:
        tree[node] = A[start]
        return
    
    mid = (start + end) // 2

    # mid 기준으로 자식 노드 내려가기
    build(node*2,start,mid)
    build(node*2+1,mid+1,end)

    tree[node] = tree[node*2] + tree[node*2+1]

# lazy 값 전파 함수
def propagate(node,start,end):
    # lazy 값이 있으면 전파
    if lazy[node] != 0:
        tree[node] += (end - start + 1)*lazy[node]

        # leaf가 아니면 자식에게 lazy값 전파
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]

        # lazy 값 전파 후 0으로 초기화
        lazy[node] = 0

# tree 업데이트 함수
def update(node,start,end,left,right,diff):
    # lazy 값 전파
    propagate(node,start,end)
    
    # 범위를 벗어나면 종료
    if right < start or end < left:
        return
    
    # 범위 내로 들어오면 tree 업데이트
    if left <= start and end <= right:
        tree[node] += (end - start + 1) * diff
        # 자식 노드가 있으면 계산 안하고 lazy 값만 추가
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    
    mid = (start + end) // 2

    update(node*2,start,mid,left,right,diff)
    update(node*2+1,mid+1,end,left,right,diff)

    tree[node] = tree[node*2] + tree[node*2+1]

# 질의 출력하기
def query(node,start,end,target):
    # lazy 값 전파
    propagate(node,start,end)

    if start == end:
        return tree[node]
    
    mid = (start + end) // 2

    if target <= mid:
        return query(node*2,start,mid,target)
    else:
        return query(node*2+1,mid+1,end,target)

# 세그먼트 트리 작성
build(1,0,N-1)

M = int(input())

for _ in range(M):
    q = list(map(int,input().split()))
    if q[0] == 1:
        i,j,k = q[1],q[2],q[3]
        update(1,0,N-1,i-1,j-1,k)

    elif q[0] == 2:
        x = q[1]
        ans = query(1,0,N-1,x-1)
        print(ans)