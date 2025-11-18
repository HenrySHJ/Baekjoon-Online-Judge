import sys
input = sys.stdin.readline

N = int(input())
DP = [0]*(N+1)
parent = [0]*(N+1)

for i in range(2,N+1):
    DP[i] = DP[i-1] + 1
    parent[i] = i-1

    # i가 2로 나누어떨어질 때
    if i % 2 == 0 and DP[i] > DP[i//2] + 1:
        DP[i] = DP[i//2] + 1
        parent[i] = i//2

    # i가 3으로 나누어떨어질 때
    if i % 3 == 0 and DP[i] > DP[i//3] + 1:
        DP[i] = DP[i//3] + 1
        parent[i] = i//3
    
print(DP[N])

count = N
while count != 0:
    print(count,end=' ')
    count = parent[count]