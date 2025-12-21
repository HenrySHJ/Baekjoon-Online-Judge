import sys
input = sys.stdin.readline

INF = sys.maxsize

N = int(input())

friend = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    friend[i][i] = 0

while True:
    a,b = map(int,input().split())

    if a == -1 and b == -1:
        break

    friend[a][b] = 1
    friend[b][a] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if friend[i][j] > friend[i][k] + friend[k][j]:
                friend[i][j] = friend[i][k] + friend[k][j]

ans = [0]*(N+1)
min_point = INF
for i in range(1,N+1):
    ans[i] = max(friend[i][1:])
    min_point = min(min_point,ans[i])

print(min_point,ans.count(min_point))

for i in range(1,N+1):
    if ans[i] == min_point:
        print(i,end=' ')