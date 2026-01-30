import sys
input = sys.stdin.readline

MOD = 9901

N,M = map(int,input().split())

# 칸 개수가 홀수면 채우기가 불가능
if (N * M) % 2 == 1:
    print(0)
    sys.exit()

# DP[i][mask] : 현재 채우려는 칸 i, 현재 상태가 mask일때 경우의 수
DP = [[0] * (1 << M) for _ in range(N * M + 1)]
DP[0][0] = 1  # 초기화

for i in range(N * M):
    for mask in range(1 << M):
        # 현재까지 전파되지 않은 경우 건너뛰기
        if DP[i][mask] == 0:
            continue
        
        # 현재 상태가 채워져있는 경우 다음 비트로 넘기기
        if mask & 1:
            DP[i + 1][mask >> 1] = (DP[i + 1][mask >> 1] + DP[i][mask]) % MOD
        else:
            # 타일을 세로로 놓기
            # 아래 칸은 M개 뒤에 있으므로 M-1번째 비트를 1로 만들기
            nmask = (mask >> 1) | (1 << (M - 1))
            DP[i + 1][nmask] = (DP[i + 1][nmask] + DP[i][mask]) % MOD
                
            # 타일을 가로로 놓기
            # 맨 오른쪽 칸이 아니고, 옆 칸이 비어있어야 함
            if (i % M) != M - 1 and not (mask & 2):
                nmask = (mask >> 2)
                DP[i + 2][nmask] = (DP[i + 2][nmask] + DP[i][mask]) % MOD

# 정답 출력 (다 채운 칸에서 더 이상 튀어나온 부분 없음)
print(DP[N * M][0])