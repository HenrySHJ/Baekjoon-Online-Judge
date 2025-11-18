import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)

DP = [[0]*(N+1) for _ in range(N+1)]

# 문자 개수 == 1
for i in range(1,N+1):
    DP[i][i] = 1

# 문자 개수 == 2
for i in range(1, N):
    if A[i] == A[i+1]:
        DP[i][i+1] = 1

# 문자 개수 >= 3
for length in range(3,N+1):
    for i in range(1,N-length+2):
        j = i + length - 1
        # 추가되는 마지막이 처음과 같고 & 제외한 부분이 팰린드롬이면
        if A[i] == A[j] and DP[i+1][j-1]:
            DP[i][j] = 1

M = int(input())
for _ in range(M):
    S,E = map(int,input().split())
    print(DP[S][E])