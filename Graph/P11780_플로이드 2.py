import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

cost = [[INF] * (N + 1) for _ in range(N + 1)]
nxt = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    cost[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    if cost[a][b] > c:
        cost[a][b] = c
        nxt[a][b] = b

# 플로이드 워셜
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if cost[i][k] + cost[k][j] < cost[i][j]:
                cost[i][j] = cost[i][k] + cost[k][j]
                nxt[i][j] = nxt[i][k]  # i -> j는 k를 경유함

#  최단 거리 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if cost[i][j] == INF:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print()

#  경로 복원 및 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if cost[i][j] == INF or i == j:
            print(0)
            continue

        route = [i]
        cur = i  # i 원본을 바꾸지 않게 별도 변수 사용
        while cur != j:  # cur은 경유점을 의미, j면 도착점에 도달
            cur = nxt[cur][j]
            route.append(cur)

        print(len(route), *route)
