import sys
input = sys.stdin.readline

def level_check(line, N, L):
    # visited로 경사로 설치 여부 확인
    visited = [False]*N 
    for i in range(N - 1):
        # 높이가 같으면 건너뛰기
        if line[i] == line[i+1]:
            continue
            
        # 경사 차이가 1보다 크면 종료
        if abs(line[i] - line[i+1]) > 1:
            return False
        
        # 내리막길
        if line[i] > line[i+1]:
            temp = line[i+1]
            # i+1에서 i+L까지 이동 가능한지 확인
            for j in range(i + 1, i + 1 + L):
                # 범위를 벗어나거나 다르거나 이미 경사로가 깔린 경우
                if j >= N or line[j] != temp or visited[j]:
                    return False
                visited[j] = True 
                
        # 오르막길
        elif line[i] < line[i+1]:
            temp = line[i]
            # i에서 i-L+1까지 이동 가능한지 확인
            for j in range(i, i - L, -1):
                # 범위를 벗어나거나 층이 다르거나 이미 경사로가 깔린 경우
                if j < 0 or line[j] != temp or visited[j]:
                    return False
                visited[j] = True 
                
    return True

N,L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 가로 줄
for row in board:
    if level_check(row,N,L):
        ans += 1

# 세로 줄
for j in range(N):
    col = [board[i][j] for i in range(N)]
    if level_check(col,N,L):
        ans += 1

print(ans)