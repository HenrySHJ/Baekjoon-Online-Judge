import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)

N, M, K = map(int, input().split())

work_graph = [[] for _ in range(N * 2 + 1)]
for i in range(1, N + 1):
    info = list(map(int, input().split()))

    for j in range(1, info[0] + 1):
        work_graph[i].append(info[j])

matched = [-1] * (M + 1)

def DFS(now):
    for nxt in work_graph[now]:
        if visited[nxt]:
            continue

        visited[nxt] = True

        if matched[nxt] == -1 or DFS(matched[nxt]):
            matched[nxt] = now
            return True
        
    return False

ans = 0
for i in range(1, N + 1):
    visited = [False] * (M + 1)
    
    if DFS(i):
        ans += 1

count = 0
for i in range(1, N + 1):
    visited = [False] * (M + 1)

    if DFS(i):
        count += 1
        ans += 1

        if count == K:
            break

print(ans)