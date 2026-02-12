import sys
input = sys.stdin.readline

# 퀸 배치하기
def putQueen(row):
    global ans

    # 마지막 열까지 배치가 끝나면 정답 추가
    if row == N:
        ans += 1
        return
    
    # 퀸은 하나의 열에 하나만 존재 가능
    for col in range(N):
        # 퀸 행 조건 / 대각 조건(row + col 일정 / row - col 일정) 확인
        if not rowCheck[col] and not diaCheck1[row + col] and not diaCheck2[row - col]:
            rowCheck[col] = True
            diaCheck1[row + col] = True
            diaCheck2[row - col] = True

            # 다음 열 퀸 배치
            putQueen(row + 1)

            # 백트래킹
            rowCheck[col] = False
            diaCheck1[row + col] = False
            diaCheck2[row - col] = False

N = int(input())

rowCheck = [False] * N
diaCheck1 = [False] * N * 2
diaCheck2 = [False] * N * 2

ans = 0
putQueen(0)
print(ans)