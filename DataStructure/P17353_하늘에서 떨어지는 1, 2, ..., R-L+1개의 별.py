import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 세그먼트 트리 채우기
def build(node,start,end):
    # leaf 노드 채우기
    if start == end:
        tree[node] = B[start]
        return

    mid = (start + end) // 2

    # 리프 노드까지 계속 뻗기
    build(node*2,start,mid)
    build(node*2+1,mid+1,end)
    
    # 상위 노드 채워나가기
    tree[node] = tree[node*2] + tree[node*2+1]

# 노드 값 수정하면서 lazy 값 전파
def propagate(node,start,end):
    # 해당 노드의 lazy 값이 있을 때
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]

        # 하위 노드 존재하면 lazy 전파
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]

        # 전파 후 0으로 세팅
        lazy[node] = 0

# 트리 업데이트 함수
def update(node,start,end,left,right,val):
    # lazy값 존재하면 전파
    propagate(node,start,end)

    # 구간 벗어나면 return
    if start > right or left > end:
        return
    
    # 구간 내로 들어오면
    if left <= start and end <= right:
        lazy[node] += val
        propagate(node,start,end)
        return
    
    mid = (start + end) // 2

    # 리프 노드까지 계속 뻗기
    update(node*2, start, mid, left, right, val)
    update(node*2+1, mid + 1, end, left, right, val)

    # 상위 노드 채워나가기
    tree[node] = tree[node*2] + tree[node*2+1]

# 트리 질의 함수
def query(node,start,end,left,right):
    # lazy값 존재하면 전파
    propagate(node,start,end)

    # 구간을 벗어나면 return
    if start > right or left > end:
        return 0
    
    # 구간 안에 들어오면
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2

    # mid 기준 구간 나눠서 탐색
    return query(node*2,start,mid,left,right) + query(node*2+1,mid+1,end,left,right)

N = int(input())
A = [0] + list(map(int,input().split()))

# 차분 배열
B = [0]*(N+2)
for i in range(1,N+1):
    B[i] = A[i] - A[i-1]

tree = [0]*((N+1)*4)
lazy = [0]*((N+1)*4)

build(1,1,N)

M = int(input())

for _ in range(M):
    q = list(map(int,input().split()))

    if q[0] == 1:
        l,r = q[1],q[2]
        update(1, 1, N, l, r, 1)

        # r+1 지점에서 등차수열의 마지막 값 빼주기
        if r + 1 <= N:
            update(1, 1, N, r + 1, r + 1, -(r - l + 1))

    elif q[0] == 2:
        x = q[1]
        # 1부터 x까지의 구간 합 : A[x]의 현재 값
        print(query(1, 1, N, 1, x))