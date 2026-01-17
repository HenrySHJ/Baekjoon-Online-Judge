import sys
input = sys.stdin.readline

N = int(input())
board = [list(input().split()) for _ in range(N)]

dx = [1,0]
dy = [0,1]

min_ans = sys.maxsize
max_ans = -sys.maxsize

def DFS(x,y,cur):
    global min_ans,max_ans

    if x == N-1 and y == N-1:
        max_ans = max(max_ans,cur)
        min_ans = min(min_ans,cur)

    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < N:
            for k in range(2):
                nnx = nx + dx[k]
                nny = ny + dy[k]

                if 0 <= nnx < N and 0 <= nny < N:
                    if board[nx][ny] == '+':
                        DFS(nnx,nny,cur + int(board[nnx][nny]))
                    elif board[nx][ny] == '-':
                        DFS(nnx,nny,cur - int(board[nnx][nny]))
                    elif board[nx][ny] == '*':
                        DFS(nnx,nny,cur * int(board[nnx][nny]))
            
DFS(0,0,int(board[0][0]))
print(max_ans,min_ans)