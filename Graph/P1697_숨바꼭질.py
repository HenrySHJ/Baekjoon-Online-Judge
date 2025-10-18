from collections import deque

N,K = map(int,input().split())
visited = [False]*(100001)
def BFS(v):
    queue = deque()
    queue.append((v,0))
    visited[v] = True
    while queue:
        pos, sec = queue.popleft()
        if pos == K:
            return sec

        for next_pos in (pos-1, pos+1, pos*2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, sec+1))

print(BFS(N))