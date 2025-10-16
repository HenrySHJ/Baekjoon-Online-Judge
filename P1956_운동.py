import sys
input = sys.stdin.readline
V,E = map(int,input().split())

road = [[sys.maxsize]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    road[a][b] = c

for K in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            # i -> K -> i의 사이클 존재 검사
            if road[i][K] != sys.maxsize and road[K][j] != sys.maxsize:
                road[i][j] = min(road[i][j],road[i][K]+road[K][j])

ans = sys.maxsize
for i in range(1,V+1):
    for j in range(1,V+1):
        if i != j and road[i][j] != sys.maxsize and road[j][i] != sys.maxsize:
            ans = min(ans,road[i][j]+road[j][i])

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)