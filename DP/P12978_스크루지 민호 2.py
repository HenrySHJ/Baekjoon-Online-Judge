import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

road = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(N-1):
    u,v = map(int,input().split())
    road[u].append(v)
    road[v].append(u)

# DP[i][j] : i번째에 경찰서를 j가 미설치:0, 설치:1) 최소 개수
DP = [[0]*2 for i in range(N+1)]

def DFS(node):
    visited[node] = True
    DP[node][0] = 0
    DP[node][1] = 1
    

    for next in road[node]:
        if visited[next]:
            continue
        DFS(next)
        DP[node][0] += DP[next][1]
        DP[node][1] += min(DP[next][0],DP[next][1])

DFS(1)
print(min(DP[1][0], DP[1][1]))