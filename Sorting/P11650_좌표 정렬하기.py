N = int(input())

coor = []
for _ in range(N):
    x,y = map(int,input().split())
    coor.append((x,y))

coor.sort()
for i in range(N):
    print(*coor[i])