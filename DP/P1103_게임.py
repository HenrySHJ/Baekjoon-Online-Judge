import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N,M = map(int,input().split())
board = [list(input().strip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
DP = [[0]*M for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def DFS(x,y):
    # 좌표 유효성 검사
    if not (0 <= x < N and 0 <= y < M):
        return 0
    
    # 구멍 검사
    if board[x][y] == 'H':
        return 0
    
    # 이미 방문한 경우 -> 루프
    if visited[x][y]:
        print(-1)
        sys.exit()

    # 이미 계산된 적이 있는 경우
    if DP[x][y] != 0:
        return DP[x][y]
    
    visited[x][y] = True
    count = 0

    for k in range(4):
        nx = x + dx[k]*int(board[x][y])
        ny = y + dy[k]*int(board[x][y])
        count = max(count,DFS(nx,ny))
    
    visited[x][y] = False  # 방문 여부는 탐색에 한해서
    DP[x][y] = count + 1
    return DP[x][y]

print(DFS(0,0))