import sys
input = sys.stdin.readline

N = int(input())
a,b = list(map(int,input().split()))

M = int(input())
target = [int(input()) for _ in range(M)]

# DP[i][j][k] : i번째 해결 이후 열린 문이 j(왼),k(오)일때 최소로 움직인 횟수
DP = [[[sys.maxsize]*(N+1) for _ in range(N+1)] for _ in range(M+1)]
DP[0][a][b] = 0

for i in range(M):
    t = target[i]
    for j in range(1,N+1):
        for k in range(1,N+1):
            if DP[i][j][k] == sys.maxsize:
                continue
            
            # 현재까지 최소 누적 움직인 횟수
            move = DP[i][j][k]

            # 왼쪽 문을 움직이기
            DP[i+1][t][k] = min(DP[i+1][t][k], move + abs(j-t))
            
            # 오른쪽 문을 움직이기
            DP[i+1][j][t] = min(DP[i+1][j][t], move + abs(k-t))

ans = sys.maxsize
for i in range(1,N+1):
    for j in range(1,N+1):
        ans = min(ans,DP[M][i][j])

print(ans)