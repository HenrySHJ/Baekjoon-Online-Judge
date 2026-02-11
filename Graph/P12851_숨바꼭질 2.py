import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

def BFS(now):
    queue = deque()
    queue.append(now)

    # 방문한 시간 저장
    visited = [-1] * 100001
    visited[now] = 0

    time = sys.maxsize
    count = 0

    while queue:
        cur = queue.popleft()

        # 목표 장소 도달
        if cur == K:
            time = visited[cur]
            count += 1
            continue

        for nxt in [cur - 1, cur + 1, cur * 2]:
            if 0 <= nxt <= 100000:
                # 미방문한 장소거나 다른 경우의 수로 같은 시간에 방문하는 경우
                if visited[nxt] == -1 or visited[nxt] == visited[cur] + 1:
                    visited[nxt] = visited[cur] + 1
                    queue.append(nxt)

    return time, count

# 정답 출력
second, answer = BFS(N)
print(second)
print(answer)