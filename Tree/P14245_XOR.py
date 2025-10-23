N = int(input())

A = list(map(int,input().split()))
tree = [0]*(4*N)
lazy = [0]*(4*N)

# 리프 노드 채우고 역순으로 올라가며 상위 노드 채우기
def build(node, start, end):
    if start == end:
        tree[node] = A[start]
        return
    mid = (start + end) // 2

    build(node*2, start, mid)
    build(node*2+1, mid+1, end)

    tree[node] = tree[node*2] ^ tree[node*2+1]

build(1,0,N-1)

# start ~ end가 리프 노드 범위 / l, r = search 범위
def update(node, start, end, l, r, val):
    # 해당 노드 번호에 lazy[node]가 있다면 적용
    if lazy[node] != 0:
        # XOR 연산을 짝수번 실행하면 원래 숫자로 돌아옴
        if (end - start + 1) % 2 == 1:
            tree[node] ^= lazy[node]
        # lazy[자식 노드] : XOR 연산
        if start != end:
            lazy[node*2] ^= lazy[node]
            lazy[node*2+1] ^= lazy[node]
        # 적용 후 0으로
        lazy[node] = 0

    # start 또는 end가 search 범위를 넘어서면
    if r < start or end < l:
        return
    
    # start와 end가 search 범위에 들어왔을 때
    if l <= start and end <= r:
        # XOR 연산을 짝수번 실행하면 원래 숫자로 돌아옴
        if (end - start + 1) % 2 == 1:
            tree[node] ^= val
        # lazy[자식 노드] : XOR 연산
        if start != end:
            lazy[node*2] ^= val
            lazy[node*2+1] ^= val
        return
    
    mid = (start + end) // 2

    update(node*2, start, mid, l, r, val)
    update(node*2+1, mid+1, end, l, r, val)

    tree[node] = tree[node*2] ^ tree[node*2+1]

# 출력
def query(node, start, end, idx):
    # lazy에 저장된 값이 있을 때
    if lazy[node] != 0:
        # XOR 연산을 짝수번 실행하면 원래 숫자로 돌아옴
        if (end - start + 1) % 2 == 1:
            tree[node] ^= lazy[node]
        # 리프 노드가 존재하면 리프에 lazy값 전달
        if start != end:
            lazy[node*2] ^= lazy[node]
            lazy[node*2+1] ^= lazy[node]
        # 적용 후 0으로
        lazy[node] = 0
    # 리프에 도달하면 반환
    if start == end:
        return tree[node]
    
    mid = (start + end) // 2

    # idx에 맞게 분할하기
    if idx <= mid:
        return query(node*2, start, mid, idx)
    else:
        return query(node*2+1, mid+1, end, idx)

M = int(input())

for _ in range(M):
    temp = list(map(int,input().split()))
    t = temp[0]
    if t == 1:
        a, b, c = temp[1],temp[2],temp[3]
        update(1,0,N-1,a,b,c)

    elif t == 2:
        a = temp[1]
        print(query(1,0,N-1,a))