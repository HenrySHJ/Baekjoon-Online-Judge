import sys
input = sys.stdin.readline

MOD = 1000000007
memo = {0: 0, 1: 1, 2: 1}

def fibo(n):
    # 한번 나온 숫자는 메모제이션으로 기록하기
    if n in memo:
        return memo[n]

    memo[n] = (fibo(n - n // 2) * fibo(n // 2 + 1) + fibo(n - 1 - n // 2) * fibo (n // 2)) % MOD

    return memo[n]

N = int(input())

print(fibo(N))