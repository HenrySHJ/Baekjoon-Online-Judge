import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)

N, M = map(int, input().split())

work_graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    info = list(map(int, input().split()))

    work_graph[i] = info[1:]

# matched[j] : j번째 일을 맡은 사람 i
matched = [-1] * (M + 1)

# 이분 매칭 DFS
def DFS(now):
    for nxt in work_graph[now]:
        if visited[nxt]:
            continue

        visited[nxt] = True

        # 아직 매칭이 안된 일 / 매칭된 일을 맡은 사람이 다른 일을 할 수 있는 경우
        if matched[nxt] == -1 or DFS(matched[nxt]):
            matched[nxt] = now
            return True
        
    return False

ans = 0
for i in range(1, N + 1):
    for _ in range(2):
        visited = [False] * (M + 1)
        if DFS(i):
            ans += 1
        
print(ans)