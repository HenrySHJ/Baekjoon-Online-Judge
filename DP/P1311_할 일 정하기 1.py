import sys
input = sys.stdin.readline

N = int(input())

# D[i][j] : i번 사람이 j번 일을 할때 드는 비용
D = [list(map(int,input().split())) for _ in range(N)]

# DP[mask] : 현재 mask(배정된 사람)에 대한 최소 비용
DP = [sys.maxsize]*(1<<N)
DP[0] = 0

for mask in range(1<<N):
    if DP[mask] == sys.maxsize:
        continue

    person = mask.bit_count()
    if person >= N:
        continue

    for j in range(N):
        # 현재 겹치는 비트 부분이 없는 경우에만
        if mask & (1<<j) == 0:
            DP[mask|(1<<j)] = min(DP[mask|(1<<j)],DP[mask]+D[person][j])
    
print(DP[(1<<N)-1])