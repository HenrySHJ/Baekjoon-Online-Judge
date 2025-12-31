import sys
input = sys.stdin.readline

MOD = 1000000007

N = int(input())
A = list(map(int, input().split()))
A.sort()
    
# 2의 거듭제곱 미리 계산
pow2 = [1] * N
for i in range(1, N):
    pow2[i] = (pow2[i-1]*2) % MOD
        
ans = 0
for i in range(N):
    # A[i]가 최댓값 : pow2[i], A[i]가 최솟값 : pow2[N-1-i]
    temp = (A[i]*(pow2[i] - pow2[N-1-i])) % MOD
    ans = (ans + temp) % MOD
        
    print(ans)