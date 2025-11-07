import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
A = list(map(int,input().split()))
tree = [[] for _ in range(N)]
DP = [0]*N

# tree[상사] = 직원
for i in range(1,N):
    tree[A[i]].append(i)

def DFS(v):
    if not tree[v]:
        DP[v] = 0
        return 0

    temp = []
    for next in tree[v]:
        temp.append(DFS(next))

    temp.sort(reverse=True)  # 오래걸리는 서브트리에게 먼저 전화

    best = 0
    # 서브트리 수 + 시간 중 최대 시간 반환
    for i, t in enumerate(temp):
        best = max(best, t + i + 1)

    DP[v] = best
    return best

print(DFS(0))