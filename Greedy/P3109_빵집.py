import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

R,C = map(int,input().split())
grid = [list(input().strip()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]

# 위쪽을 먼저 탐색해서 경우의 수 확보
dx = [-1,0,1]
ans = 0

def DFS(x,y):
    if y == C-1:
        return True
    
    for k in range(3):
        nx = x + dx[k]
        ny = y + 1
        # 좌표 유효성 검사 / 미방문 여부 검사 / 빵집 검사
        if 0 <= nx < R and not visited[nx][ny] and grid[nx][ny] != 'x':
            visited[nx][ny] = True
            if DFS(nx, ny):
                return True
            
    return False

for i in range(R):
    if DFS(i,0):
        ans += 1

print(ans)