import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

# 트리 기본 세팅
treeHeight = 0
length = N
while length != 0:
    length //= 2
    treeHeight += 1

treeSize = 1 << (treeHeight + 1)
leafstart = treeSize // 2 - 1
tree = [0] * (treeSize + 1)
lazy = [0] * (treeSize + 1)

# 리프 노드 채우기
for i in range(leafstart + 1, leafstart + N + 1):
    tree[i] = int(input())

# 상위 노드 채우기
def build_tree(i):
    while i > 1:
        tree[i // 2] += tree[i]
        i -= 1
build_tree(treeSize - 1)

# lazy 반영 함수
def propagate(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:  # 리프 노드가 아니면 자식에게 lazy 전파
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0

# 구간 업데이트
def update_range(node, start, end, left, right, diff):
    propagate(node, start, end)
    if right < start or end < left:
        return
    if left <= start and end <= right:
        tree[node] += (end - start + 1) * diff
        if start != end:
            lazy[node * 2] += diff
            lazy[node * 2 + 1] += diff
        return
    mid = (start + end) // 2
    update_range(node * 2, start, mid, left, right, diff)
    update_range(node * 2 + 1, mid + 1, end, left, right, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

# 구간 합
def query(node, start, end, left, right):
    propagate(node, start, end)
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)

# 연산 처리
for _ in range(M + K):
    temp = list(map(int, input().split()))
    if temp[0] == 1:  # 구간에 더하기
        b, c, d = temp[1], temp[2], temp[3]
        update_range(1, 1, leafstart+1, b, c, d)
    else:  # 구간 합 구하기
        b, c = temp[1], temp[2]
        print(query(1, 1, leafstart+1, b, c))