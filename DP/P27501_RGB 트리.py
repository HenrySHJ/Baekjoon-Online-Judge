import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

tree = [[0,0,0]]+[list(map(int,input().split())) for _ in range(N)]

# DP[i][j] : i번째 전구가 j(0: R, 1: G, 2: B)일때 최대 아름다움
DP = [[0]*3 for _ in range(N+1)]

# 트리 DP
def DFS(now):
    visited[now] = True

    for k in range(3):
        DP[now][k] = tree[now][k]

    for next in graph[now]:
        if visited[next]:
            continue
        DFS(next)
        
        DP[now][0] += max(DP[next][1],DP[next][2])
        DP[now][1] += max(DP[next][0],DP[next][2])
        DP[now][2] += max(DP[next][0],DP[next][1])

DFS(1)
print(max(DP[1]))

# 역추적
color = [-1]*(N+1)
def trace(now, parent_color):
    # 현재 노드 색 선택
    best = -1
    best_color = -1

    for c in range(3):
        # 상위 노드와 색 같은 경우 건너뛰기
        if c == parent_color:
            continue
        # 제외하고 가장 DP값이 클 때
        if DP[now][c] > best:
            best = DP[now][c]
            best_color = c

    color[now] = best_color

    # 하위 노드 탐색
    for next in graph[now]:
        # color 값이 -1이면 미방문
        if color[next] != -1:
            continue
        trace(next, best_color)

trace(1,-1)
convert = ['R','G','B']
print(''.join(convert[color[i]] for i in range(1, N+1)))