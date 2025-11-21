import sys
input = sys.stdin.readline

C,N = map(int,input().split())
MAX = C+100

info = []
for _ in range(N):
    a,b = map(int,input().split())
    info.append((a,b))

# DP[i] : 고객 i명을 얻기 위한 최소 금액
DP = [sys.maxsize]*(MAX+1)
DP[0] = 0

for a,b in info:
    for i in range(b,MAX+1):
        DP[i] = min(DP[i], DP[i-b] + a)

print(min(DP[C:]))