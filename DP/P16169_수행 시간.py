import sys
input = sys.stdin.readline

N = int(input())

level = [[] for _ in range(N+1)]   

for i in range(1,N+1):
    r,t = map(int,input().split())
    level[r].append((i,t))

DP = [0]*(N+1)
for r in range(1,N+1):
    for (i,t) in level[r]:
        DP[i] = t if DP[i] == 0 else DP[i]

    if r < N:
        for (i, t) in level[r]:
            for (j,nt) in level[r+1]:
                new_time = DP[i] + (i-j)**2 + nt
                DP[j] = max(DP[j], new_time)

print(max(DP))