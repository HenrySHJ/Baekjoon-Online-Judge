import sys
input = sys.stdin.readline

N,T = map(int,input().split())

Drivers = [list(input().split()) for _ in range(N)]
Drivers[0][1] = int(Drivers[0][1])
for i in range(1,N):
    Drivers[i][1] = (Drivers[i-1][1] + int(Drivers[i][1])) % T

Drivers.sort(key=lambda x:x[1])

ans = []
if 0 < T - Drivers[N-1][1] <= 1000:
    ans.append(Drivers[0][0])

for i in range(N-1):
    if 0 < Drivers[i+1][1] - Drivers[i][1] <= 1000:
        ans.append(Drivers[i+1][0])
    
ans.sort()
if ans:
    print(*ans)
else:
    print(-1)