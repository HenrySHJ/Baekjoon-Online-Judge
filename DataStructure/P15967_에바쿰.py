import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# Segment Tree에 A 리스트 정보 바탕 입력
def build(node, start, end):
    # Tree의 leaf 노드에 정보 입력
    if start == end:
        tree[node] = A[start]
        return
    
    mid = (start + end) // 2

    build(node*2, start, mid)
    build(node*2 + 1, mid + 1, end)

    # 상위 노드가 리프 노드의 합 저장
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

# 저장된 lazy 값 전파
def propagate(node, start, end):
    # 저장된 lazy 값이 존재하는 경우
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]

        # 하위 노드가 존재하는 경우 lazy 전파
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]

        # 전파 후 lazy 값 초기화
        lazy[node] = 0

# left ~ right일에 value만큼 맞은 양 늘리기
def update(node, start, end, left, right, value):
    # lazy 값이 존재하면 전파
    propagate(node, start ,end)

    # 범위를 벗어난 경우
    if start > right or end < left:
        return
    
    # 범위 내로 들어온 경우
    if left <= start and end <= right:
        lazy[node] += value
        propagate(node, start, end)
        return
    
    mid = (start + end) // 2

    update(node * 2, start, mid ,left, right, value)
    update(node * 2 + 1, mid + 1, end ,left, right, value)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]

# left일 ~ right일 사이에 맞은 양 반환
def query(node, start, end, left, right):
    # lazy 값이 존재하면 전파
    propagate(node, start ,end)

    # 범위를 벗어난 경우
    if start > right or end < left:
        return 0
    
    # 범위 내로 들어온 경우
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2

    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)

N, Q1, Q2 = map(int, input().split())
A = list(map(int, input().split()))

# A 리스트 정보를 세그먼트 트리에 옮기기
tree = [0] * (4 * N)
lazy = [0] * (4 * N)
build(1, 0 , N - 1)

# 업데이트 & 출력
for _ in range(Q1 + Q2):
    Q = list(map(int, input().split()))

    if Q[0] == 1:
        n, m = Q[1], Q[2]
        ans = query(1, 0 , N - 1, n - 1, m - 1)
        print(ans)

    elif Q[0] == 2:
        s, e, l = Q[1], Q[2], Q[3]
        update(1, 0, N - 1, s - 1, e - 1, l)