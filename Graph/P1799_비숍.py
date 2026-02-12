import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 체스판 타일 색에 따른 분류
black = []
white = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            continue
        
        # 합이 짝수면 검은 칸
        if (i + j) % 2 == 0:
            black.append((i, j))
        # 합이 홀수면 흰 칸
        else:
            white.append((i, j))

# x, y 좌표 합을 기준으로 비숍 배치
def bishop(color, index, count):
    global ans
    
    # 정답 갱신 시키기
    if index == len(color):
        ans = max(ans, count)
        return

    x, y = color[index]

    # 현재 좌표에 비숍 배치하는 경우
    if diag1[x + y] == 0 and diag2[x - y] == 0:
        diag1[x + y] = 1
        diag2[x - y] = 1

        # 비숍 배치 후 재귀
        bishop(color, index + 1, count + 1)

        # 백트래킹으로 비숍 배치 정보 전 단계로 업데이트
        diag1[x + y] = 0
        diag2[x - y] = 0
    
    # 현재 좌표에 비숍 배치하지 않는 경우
    bishop(color, index + 1, count)

# x, y 좌표의 합, 차를 이용한 배치 가능 여부 확인
diag1 = [0] * (N * 2)
diag2 = [0] * (N * 2)

ans = 0
bishop(black, 0, 0)
black_ans = ans

ans = 0
bishop(white, 0, 0)
white_ans = ans

print(black_ans + white_ans)