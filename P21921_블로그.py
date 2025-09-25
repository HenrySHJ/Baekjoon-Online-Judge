N,X = map(int,input().split())

A = list(map(int,input().split()))
A.insert(0,0)

# 합 배열 S
S = [0]*(N+1)
for i in range(1,N+1):
    S[i] = A[i] + S[i-1]

# 1~X 번 사이의 합
s = 1
e = X

ans = 0
count = 0
while e < N+1:
    M = S[e] - S[s-1]
    if ans < M:
        ans = M
        count = 1
    elif ans == M:
        count += 1
    s += 1
    e += 1

if ans == 0:
    print('SAD')
else:
    print(ans)
    print(count)