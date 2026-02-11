import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(input().strip()) for _ in range(R)]
alphabet_visited = [False] * 26

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, count):
    global ans
    ans = max(ans, count)

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 좌표 유효성 검사
        if 0 <= nx < R and 0 <= ny < C:
            # 중복 알파벳 검사
            idx = ord(board[nx][ny]) - ord('A')
            
            if alphabet_visited[idx]:
                continue

            alphabet_visited[idx] = True
            DFS(nx, ny, count + 1)

            alphabet_visited[idx] = False

ans = 0  

# 시작점 처리
start_idx = ord(board[0][0]) - ord('A')
alphabet_visited[start_idx] = True
DFS(0, 0, 1)

print(ans)