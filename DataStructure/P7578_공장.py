import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

# 트리의 높이 구하기
tree_size = 1
while tree_size < N:
    tree_size *= 2

tree = [0]*(2*tree_size)

# 바텀 - 업
# 업데이트 함수
def update(i):
    # 세그먼트 트리의 인덱스에 맞게 변환
    idx = i + tree_size
    tree[idx] += 1

    # 상위 노드 재연산
    while idx > 1:
        idx //= 2
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]

# 질의 함수
def query(l, r):
    res = 0

    # 세그먼트 트리의 인덱스에 맞게 변환
    l += tree_size
    r += tree_size

    # l ~ r 합 구하기
    while l <= r:
        if l % 2 == 1: 
            res += tree[l]
            l += 1
        if r % 2 == 0: 
            res += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return res

# A : {기계 : 인덱스}
location = {m: i for i, m in enumerate(A)}

# 세그먼트 트리
tree = [0]*(4*N)

ans = 0
for m in B:
    target = location[m]
    
    # tree[target] ~ tree[N-1] 합이 겹친 점 개수
    if target < N - 1:
        ans += query(target, N-1)
    
    # 트리 업데이트
    update(target)

print(ans)