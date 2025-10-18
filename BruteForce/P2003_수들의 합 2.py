N, M = map(int,input().split())
A = list(map(int,input().split()))
A.insert(0,0)
S = [0]*(N+1)
S[1] = A[1]

# 합 배열
for i in range(2,N+1):
    S[i] = S[i-1] + A[i]

# 투 포인터
s = 1
e = 1
ans = 0

while e < N+1:
    # A[s] ~ A[e]까지의 합
    if S[e] - S[s-1] == M:
        ans += 1
        e += 1
    elif S[e] - S[s-1] > M:
        s += 1
    else:
        e += 1

print(ans)