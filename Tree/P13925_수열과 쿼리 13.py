import sys
input = sys.stdin.readline

MOD = 10**9 + 7

N = int(input())
A = list(map(int,input().split()))

tree = [0]*(4*N)
lazy_add = [0]*(4*N)
lazy_mul = [1]*(4*N)
lazy_change = [None]*(4*N)

# 상위 노드 채우기
def build(node,start,end):
    if start == end:
        tree[node] = A[start] % MOD
        return
    
    mid = (start + end) // 2
    build(node*2,start,mid)
    build(node*2 + 1,mid + 1, end)

    tree[node] = (tree[node*2] + tree[node*2 + 1]) % MOD

build(1,0,N-1)

# tree에 lazy값 반영 / lazy 값 처리
def propagate(node,start,end):
    # 3번 쿼리로 인한 lazy 값 처리
    if lazy_change[node] != None:
        tree[node] = ((end - start + 1)*lazy_change[node]) % MOD
        # 하위 노드에게 전파
        if start != end:
            lazy_change[node*2] = lazy_change[node]
            lazy_change[node*2 + 1] = lazy_change[node]
            lazy_add[node*2] = 0
            lazy_add[node*2 + 1] = 0
            lazy_mul[node*2] = 1
            lazy_mul[node*2 + 1] = 1
        # lazy값 초기화
        lazy_change[node] = None

    # 2번 쿼리로 인한 lazy값 처리
    if lazy_mul[node] != 1:
        tree[node] = (tree[node] * lazy_mul[node]) % MOD
        # 하위 노드에게 전파
        if start != end:
            # lazy_change 값이 존재하면 그 값에 대신 저장해두기
            if lazy_change[node*2] != None:
                lazy_change[node*2] = lazy_change[node*2] * lazy_mul[node] % MOD
            # (N + a) * b -> N * b + N * a
            else:
                lazy_mul[node*2] = lazy_mul[node*2] * lazy_mul[node] % MOD
                lazy_add[node*2] = lazy_add[node*2] * lazy_mul[node] % MOD

            if lazy_change[node*2 + 1] != None:
                lazy_change[node*2 + 1] = lazy_change[node*2 + 1] * lazy_mul[node] % MOD
            else:
                lazy_mul[node*2 + 1] = lazy_mul[node*2 + 1] * lazy_mul[node] % MOD
                lazy_add[node*2 + 1] = lazy_add[node*2 + 1] * lazy_mul[node] % MOD 
        # lazy값 초기화
        lazy_mul[node] = 1

    # 1번 쿼리로 인한 lazy값 처리
    if lazy_add[node] != 0:
        tree[node] = (tree[node] + (end - start + 1) * lazy_add[node]) % MOD
        # 하위 노드에게 전파
        if start != end:
            # lazy_change 값이 존재하면 그 값에 대신 저장해두기
            if lazy_change[node*2] != None:
                lazy_change[node*2] = (lazy_change[node*2] + lazy_add[node]) % MOD
            else:
                lazy_add[node*2] = (lazy_add[node*2] + lazy_add[node]) % MOD

            if lazy_change[node*2 + 1] != None:
                lazy_change[node*2 + 1] = (lazy_change[node*2 + 1] + lazy_add[node]) % MOD
            else:
                lazy_add[node*2 + 1] = (lazy_add[node*2 + 1] + lazy_add[node]) % MOD
        # lazy값 초기화
        lazy_add[node] = 0

# 1번 query 처리  
def update_add(node,start,end,l,r,v):
    propagate(node, start, end)

    # 범위를 벗어나는 경우 처리
    if r < start or end < l:
        return
    
    # 리프 노드 모두가 범위에 포함될 경우
    if l <= start and end <= r:
        lazy_add[node] = (lazy_add[node] + v) % MOD
        propagate(node, start, end)
        return
    
    mid = (start + end)//2

    update_add(node*2, start, mid, l, r, v)
    update_add(node*2+1, mid+1, end, l, r, v)

    tree[node] = (tree[node*2] + tree[node*2+1]) % MOD

# 2번 query 처리  
def update_mul(node,start,end,l,r,v):
    propagate(node,start,end)

    if start > r or end < l:
        return
    
    if l <= start and end <= r:
        lazy_mul[node] = (lazy_mul[node] * v) % MOD
        propagate(node, start, end)
        return
    
    mid = (start + end) // 2

    update_mul(node*2,start,mid,l,r,v)
    update_mul(node*2 + 1,mid+1,end,l,r,v)

    tree[node] = (tree[node*2] + tree[node*2 + 1]) % MOD

# 3번 query 처리  
def update_change(node,start,end,l,r,v):
    propagate(node,start,end)

    if start > r or end < l:
        return
    
    if l <= start and end <= r:
        lazy_change[node] = v % MOD
        lazy_add[node] = 0
        lazy_mul[node] = 1
        propagate(node, start, end)
        return
    
    mid = (start + end) // 2

    update_change(node*2,start,mid,l,r,v)
    update_change(node*2 + 1,mid+1,end,l,r,v)

    tree[node] = (tree[node*2] + tree[node*2 + 1]) % MOD

# 4번 출력 처리
def query(node, start, end, l, r):
    propagate(node, start, end)

    if r < start or end < l:
        return 0
    
    if l <= start and end <= r:
        return tree[node] % MOD
    
    mid = (start + end)//2

    return (query(node*2, start, mid, l, r) + query(node*2+1, mid+1, end, l, r)) % MOD

M = int(input())
for _ in range(M):
    temp = list(map(int,input().split()))
    q,x,y = temp[0],temp[1],temp[2]
    if q == 1:
        v = temp[3]
        update_add(1,0,N-1,x-1,y-1,v)

    elif q == 2:
        v = temp[3]
        update_mul(1,0,N-1,x-1,y-1,v)

    elif q == 3:
        v = temp[3]
        update_change(1,0,N-1,x-1,y-1,v)

    elif q == 4:
        print(query(1,0,N-1,x-1,y-1))