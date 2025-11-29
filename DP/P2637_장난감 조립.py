import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
M = int(input())

comp = [[] for _ in range(N+1)]
indegree = [0]*(N+1)  # 위상정렬
# DP[i][j]: i를 기본 부품 j로부터 만들때 필요한 j 개수
DP = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    # comp[Y] = (X,K) : X를 만드는데 Y가 K만큼 필요
    X,Y,K = map(int,input().split())
    comp[Y].append((X,K))
    indegree[X] += 1
    
queue = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        DP[i][i] = 1
        queue.append(i)

while queue:
    now = queue.popleft()
    for next, k in comp[now]:
        for i in range(1, N+1):
            DP[next][i] += DP[now][i] * k

        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

# 완제품 N을 구성하는 기본 부품 출력
for i in range(1, N+1):
    if DP[N][i] > 0:
        print(i, DP[N][i])