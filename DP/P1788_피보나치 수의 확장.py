import sys
input = sys.stdin.readline

MOD = 1000000000

N = int(input())

if N > 0:
    DP1 = [0]*(N+1)
    DP1[1] = 1

    for i in range(2,N+1):
        DP1[i] = (DP1[i-1] + DP1[i-2]) % MOD

    print(1)
    print(DP1[N])

elif N < 0:
    N = abs(N)
    DP2 = [0]*(N+1)
    DP2[1] = 1

    for i in range(2,N+1):
        DP2[i] = (DP2[i-2] - DP2[i-1])

        if DP2[i] < 0:
            DP2[i] = (abs(DP2[i])%MOD)*-1
        else:
            DP2[i] %= MOD

    print(-1 if DP2[N] < 0 else 1)
    print(abs(DP2[N]))

else:
    print(0)
    print(0)