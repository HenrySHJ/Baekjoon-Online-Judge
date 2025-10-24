import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

tree = [0]*(4*N)
lazy = [0]*(4*N)

# 상위 노드 채우기
def build(node,start,end):
    if start == end:
        tree[node] = A[start]
        return

    mid = (start + end)//2

    build(node*2, start, mid)
    build(node*2 + 1, mid+1, end)

    tree[node] = tree[node*2] ^ tree[node*2 + 1]

build(1,0,N-1)

# lazy 처리 파트
def propagate(node,start,end):
    # lazy값이 존재한다면
    if lazy[node] != 0:
        # 하위 범위가 홀수면 XOR 연산 적용
        if (end - start + 1) % 2 == 1:
            tree[node] ^= lazy[node]
        # 하위 노드가 존재하면 lazy값 뿌리기
        if start != end:
            lazy[node*2] ^= lazy[node]
            lazy[node*2 + 1] ^= lazy[node]
        # lazy 적용 후
        lazy[node] = 0
    
# tree & lazy 업데이트하기
def update(node,start,end,l,r,k):
    # lazy 값 처리
    propagate(node,start,end)

    # 범위를 벗어나면
    if start > r or end < l:
        return
    
    # 범위 안에 들어오면
    if start >= l and end <= r:
        # 하위 범위가 홀수면 XOR 연산 적용
        if (end - start + 1) % 2 == 1:
            tree[node] ^= k
        # 하위 노드가 존재하면 lazy값 뿌리기
        if start != end:
            lazy[node*2] ^= k
            lazy[node*2 + 1] ^= k
        return
    
    mid = (start + end) // 2

    update(node*2,start,mid,l,r,k)
    update(node*2 + 1, mid + 1,end,l,r,k)

    tree[node] = tree[node*2] ^ tree[node*2 + 1]

def query(node,start,end,l,r):
    # lazy 값 처리
    propagate(node,start,end)

    # 범위를 벗어나면
    if start > r or end < l:
        return 0
    
    # 범위 내로 들어오면 
    if start >= l and end <= r:
        return tree[node]

    mid = (start + end) // 2

    return query(node*2,start,mid,l,r) ^ query(node*2 + 1,mid+1,end,l,r)

M = int(input())

for _ in range(M):
    temp = list(map(int,input().split()))
    q, i, j = temp[0],temp[1],temp[2]
    if q == 1:
        k = temp[3]
        update(1,0,N-1,i,j,k)

    elif q == 2:
        print(query(1,0,N-1,i,j))
