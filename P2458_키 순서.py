import sys
input = sys.stdin.readline
N,M = map(int,input().split())

# measure[i][j] = 1  : i < j
# measure[i][j] = -1 : i > j
# measure[i][j] = 0  : 관계 모름
measure = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    measure[a][b] = 1
    measure[b][a] = -1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            # i < k, k < j이면 i < j : 값 1로 나타내기
            if measure[i][k] == 1 and measure[k][j] == 1:
                measure[i][j] = 1
            # i > k, k > j이면 i > j : 값 -1로 나타내기
            elif measure[i][k] == -1 and measure[k][j] == -1:
                measure[i][j] = -1
                
ans = 0
for i in range(1,N+1):
    count = 0
    for j in range(1,N+1):
        if measure[i][j] == 0:
            count += 1
    # i,j가 같을 때 제외하고는 순위가 정해져있는 경우
    if count == 1:
        ans += 1

print(ans) 