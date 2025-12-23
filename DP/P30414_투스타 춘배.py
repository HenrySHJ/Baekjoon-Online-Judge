import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N,P = map(int,input().split())

A = [0]+list(map(int,input().split()))
B = [0]+list(map(int,input().split()))

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

# DP[i] = i번째 산에서 (모은 흙, 필요 흙)
DP = [[0,0] for _ in range(N+1)]

def DFS(now,prev):
    if A[now] > B[now]:
        DP[now][0] = A[now] - B[now]
    else:
        DP[now][1] = B[now] - A[now]

    for next in graph[now]:
        if next != prev:

            DFS(next,now)

            # 상위 노드에 필요한 흙 값 전달
            DP[now][1] += DP[next][1]

            # 상위 과정에서 모은 흙으로 하위 과정에 필요한 흙 메우기
            if DP[now][0] > 0 and DP[now][1] > 0:
                if DP[now][0] >= DP[now][1]:
                   DP[now][0] -= DP[now][1]
                   DP[now][1] = 0
                else:
                   DP[now][1] -= DP[now][0]
                   DP[now][0] = 0

DFS(P,-1)

# 루트 노드에서 필요한 흙이 최소 비용
print(DP[P][1])