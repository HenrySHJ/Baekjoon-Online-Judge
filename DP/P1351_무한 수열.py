import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N,P,Q = map(int,input().split())
DP = {0: 1}

def solve(n):
    if n in DP:
        return DP[n]
    # 필요한 수만 딕셔너리에 생성해서 메모리 줄이기 
    DP[n] = solve(n//P) + solve(n//Q)
    return DP[n]

print(solve(N))