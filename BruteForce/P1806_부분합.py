import sys

N,M = map(int,input().split())
A = list(map(int,input().split()))
A.insert(0,0)

# 합 배열 S
S = [0]*(N+1)
S[1] = A[1]
for i in range(2,N+1):
    S[i] = S[i-1] + A[i]

# Two-Pointer
s = 1
e = 1
ans = sys.maxsize

while e < N+1:
    if S[e] - S[s-1] >= M:
        ans = min(ans,e-s+1)
        s += 1
    else:
        e += 1

if ans == sys.maxsize:
    print(0)
else:
    print(ans)