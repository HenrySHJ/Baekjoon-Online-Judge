N = int(input())
A = list(map(int,input().split()))
v = int(input())

ans = 0
for i in range(N):
    if v == A[i]:
        ans += 1

print(ans)