N = int(input())

DP = [1] * (N + 1)

for i in range(1, N + 1):
    DP[i] = DP[i - 1] * i

ans = 0
while DP[N] != 0:
    if DP[N] % 10 == 0:
        ans += 1
        DP[N] //= 10
    else:
        break
        

print(ans)