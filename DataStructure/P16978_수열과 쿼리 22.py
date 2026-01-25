import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def build(node, start, end):
    if start == end:
        tree[node] = A[start]
        return
    
    mid = (start + end) // 2

    build(node * 2, start, mid)
    build(node * 2 + 1, mid + 1, end)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def update(node, start, end, idx, value):
    if start == end:
        tree[node] = value
        return
    
    mid = (start + end) // 2

    if idx <= mid:
        update(node * 2, start, mid, idx, value)
    else:
        update(node * 2 + 1, mid + 1, end, idx, value)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(node, start, end, left, right):
    if start > right or left > end:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2

    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)

N = int(input())
A = [0] + list(map(int,input().split()))

# A를 세그먼트 트리로
tree = [0] * (4 * N)
build(1, 1, N)

M = int(input())
update_queries = [] # 1번 쿼리 저장
sum_queries = []    # 2번 쿼리 저장
sum_count = 0

# 쿼리의 정보들을 먼저 받기
for _ in range(M):
    q = list(map(int,input().split()))

    if q[0] == 1:
        i, v = q[1], q[2]
        update_queries.append((q[1], q[2]))

    elif q[0] == 2:
        k, i, j = q[1], q[2], q[3]
        sum_queries.append((q[1], q[2], q[3], sum_count))
        sum_count += 1

# k 오름차순으로 쿼리 정리
sum_queries.sort()

ans = [0] * sum_count
cur_k = 0

for k, l, r, i in sum_queries:
    # 현재 쿼리가 원하는 k까지 업데이트
    while cur_k < k:
        idx, val = update_queries[cur_k]
        update(1, 1, N, idx, val)
        cur_k += 1
    
    # 원하는 k 상태가 되었을 때 정답 구하기
    ans[i] = query(1, 1, N, l, r)

for i in range(sum_count):
    print(ans[i])