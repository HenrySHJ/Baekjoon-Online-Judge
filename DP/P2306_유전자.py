import sys
input = sys.stdin.readline

DNA = [0]+list(input().strip())
N = len(DNA)

# DP[i][j] : DNA[i:j+1] 구간의 최대 KOI 유전자 길이
DP = [[0]*N for _ in range(N)]

# 구간 DP
for interval in range(1,N):
    # i 시작점
    for i in range(N-interval):
        # j 끝점
        j = i + interval
        
        # 조건 1&2 : 양 끝이 a-t 또는 g-c로 짝을 이루는 경우
        if (DNA[i] == 'a' and DNA[j] == 't') or (DNA[i] == 'g' and DNA[j] == 'c'):
            DP[i][j] = DP[i+1][j-1] + 2
        
        # 조건 3: 구간을 k 기준으로 쪼개서 합치는 경우
        for k in range(i,j):
            if DP[i][j] < DP[i][k] + DP[k+1][j]:
                DP[i][j] = DP[i][k] + DP[k+1][j]

print(DP[0][N-1])