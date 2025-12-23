import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def DFS(now,prev):
    for next,cost in graph[now]:
        if next != prev:
            # 상위 노드에서 잠길 때
            DP[next][0] = cost 

            DFS(next,now)
            if DP[now][1] == sys.maxsize:
                DP[now][1] = 0
            DP[now][1] += min(DP[next])

while True:
    try:
        N,C = map(int,input().split())
    except ValueError:
        break

    graph = [[] for _ in range(N+1)]

    for _ in range(N-1):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))

    # DP[i] = i번째 밸브에서 (상위 노드에서 잠그는 힘, 하위 노드를 잠그는 힘)
    DP = [[sys.maxsize,sys.maxsize] for _ in range(N+1)]
    DFS(C,-1)

    print(DP[C][1])