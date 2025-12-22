import sys
input = sys.stdin.readline

INF = sys.maxsize
N,R = map(int,input().split())

graph = [[] for _ in range(N+1)]  # 정점 연결 정보 저장
DP = [-1]*(N+1)                 # 노드 값 저장
visited = [False]*(N+1)

for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

L = int(input())

for _ in range(L):
    k,t = map(int,input().split())
    DP[k] = t

# Tree DFS
def DFS(now,depth):
    visited[now] = True

    # 깊이 홀수 : 0으로 초기화 / 짝수 : INF로 초기화
    if depth % 2 == 1 and DP[now] == -1:
        DP[now] = 0
    elif depth % 2 == 0 and DP[now] == -1:
        DP[now] = INF

    for next in graph[now]:
        if not visited[next]:

            DFS(next,depth + 1)
            
            # 깊이가 홀수면 Max / 짝수면 Min
            if depth % 2 == 1:
                DP[now] = max(DP[now],DP[next])
            else:
                DP[now] = min(DP[now],DP[next])

DFS(R,1)

Q = int(input())

for _ in range(Q):
    q = int(input())
    print(DP[q])