import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 소, 축사를 인접 그래프로
cow_graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    S = list(map(int, input().split()))

    for j in range(1, S[0] + 1):
        cow_graph[i].append(S[j])

# matched[j] = i : j번째 축사가 i번째 소랑 매칭
matched = [-1] * (M + 1)

# 이분 매칭 DFS
def DFS(now):
    for shed in cow_graph[now]:
        # 이미 검사한 축사면 건너뛰기
        if visited[shed]:
            continue

        visited[shed] = True

        # 배정되지 않은 축사거나 축사에 배정된 소를 옮길 수 있는 경우
        if matched[shed] == -1 or DFS(matched[shed]):
            matched[shed] = now
            return True
        
    return False

ans = 0
for i in range(1, N + 1):
    visited = [False] * (M + 1)

    if DFS(i):
        ans += 1

print(ans)