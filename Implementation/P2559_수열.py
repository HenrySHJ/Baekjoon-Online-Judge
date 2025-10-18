import sys

N,K = map(int,input().split())

A = list(map(int,input().split()))
A.insert(0,0)

# 합 배열
S = [0]*(N+1)
for i in range(1,N+1):
    S[i] = S[i-1] + A[i]

s = 1
e = K
ans = -sys.maxsize

while e < N+1:
    temp = S[e] - S[s-1]
    ans = max(ans,temp)
    s += 1
    e += 1

print(ans)