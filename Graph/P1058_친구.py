import sys
input = sys.stdin.readline

N = int(input())

friend = [list(input().strip()) for _ in range(N)]
D = [[0]*N for _ in range(N)]

answer = 0

for i in range(N):
    is_friend = [False]*N

    for j in range(N):
        # 직접 친구
        if friend[i][j] == 'Y':
            is_friend[j] = True
        else:
            # 친구의 친구
            for k in range(N):
                if friend[i][k] == 'Y' and friend[k][j] == 'Y':
                    is_friend[j] = True
                    break

    # 자기 자신 제외하고 카운트
    count = 0
    for j in range(N):
        if i == j:
            continue
        if is_friend[j]:
            count += 1

    answer = max(answer, count)

print(answer)
