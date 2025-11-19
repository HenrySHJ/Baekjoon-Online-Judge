import sys
input = sys.stdin.readline

N,D = map(int,input().split())
shortcut = [[] for _ in range(D+1)]

for _ in range(N):
    s,e,l = map(int,input().split())
    if e <= D:
        shortcut[s].append((e,l))

DP = [0]*(D+1)
for i in range(1,D+1):
    DP[i] = i

for i in range(D):
    DP[i+1] = min(DP[i+1],DP[i]+1)

    for e,l in shortcut[i]:
        DP[e] = min(DP[e],DP[i]+l)

print(DP[D])