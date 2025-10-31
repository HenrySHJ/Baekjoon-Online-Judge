N = int(input())

ans = N
for i in range(1,N//2+1):
    if N % i == 0:
        ans += i

print(ans)
