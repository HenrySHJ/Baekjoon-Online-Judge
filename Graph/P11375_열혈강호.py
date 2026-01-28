import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

# work_graph[i] : i가 할 수 있는 일들의 리스트
work_graph = [[] for _ in range(N + 1)]

# work_graph 채우기
for i in range(1, N + 1):
    work_able = list(map(int, input().split()))

    for j in range(1, work_able[0] + 1):
        work_graph[i].append(work_able[j])

# matched[j] = i : 특정 일 j를 맡은 사람 i
matched = [-1] * (M + 1)

# 이분 매칭 DFS
def DFS(idx):
    # 연결 가능성 검토
    for work in work_graph[idx]:
        # 이미 검사한 work면 건너뛰기
        if visited[work]:
            continue

        visited[work] = True

        # 아직 배정되지 않은 일인 경우 / 기존에 해당 일을 하던 사람이 비켜 줄 수 있는 경우
        if matched[work] == -1 or DFS(matched[work]):
            matched[work] = idx
            return True

    return False

# 개수 세기
ans = 0
for i in range(1, N + 1):
    visited = [False] * (M + 1)

    if DFS(i):
        ans += 1

print(ans)