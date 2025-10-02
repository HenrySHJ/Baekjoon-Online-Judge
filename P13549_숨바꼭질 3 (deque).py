from collections import deque

N, K = map(int, input().split())
visited = [-1] * 100001

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0 

    while queue:
        pos = queue.popleft()

        if pos == K:
            return visited[pos]

        # 순간이동 (비용 0) : 덱 앞에 넣음
        next_pos = pos * 2
        if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
            visited[next_pos] = visited[pos]
            queue.appendleft(next_pos)

        # 걷기 (비용 1) : 덱 뒤에 넣음
        for next_pos in (pos - 1, pos + 1):
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
                visited[next_pos] = visited[pos] + 1
                queue.append(next_pos)

print(bfs(N))