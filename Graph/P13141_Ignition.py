import sys
input = sys.stdin.readline

INF = sys.maxsize

N,M = map(int,input().split())

# graph[i][j] : i와 j 사이 간선 중 최소 거리
graph = [[INF]*(N+1) for _ in range(N+1)]
lines = []

for i in range(1,N+1):
    graph[i][i] = 0

for _ in range(M):
    s,e,l = map(int,input().split())

    lines.append((s,e,l))
    graph[s][e] = min(graph[s][e],l)
    graph[e][s] = min(graph[e][s],l)

# 플로이드-워셜
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

answer = float('inf')

# 발화점 k 고정
for k in range(1,N+1):
    time = 0

    # 모든 간선에 대해 점화
    for u,v,w in lines:
        t1 = graph[k][u]
        t2 = graph[k][v]

        # 발화 시간은 (세 정점의 둘레 / 2)
        burn = (t1 + t2 + w) /2

        # burn 중 최댓값이 k 정점에서의 모든 간선 태우는 시간
        time = max(time, burn)

    answer = min(answer, time)

print(answer)