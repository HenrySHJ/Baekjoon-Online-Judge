import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K,M,P = map(int,input().split())
    
    graph = [[] for _ in range(M+1)]
    indegree = [0]*(M+1)
    seq = [[0,0] for _ in range(M+1)]
    order = [1]*(M+1)
    for _ in range(P):
        A,B = map(int,input().split())
        graph[A].append(B)
        indegree[B] += 1

    queue = deque()
    for i in range(1,M+1):
        if indegree[i] == 0:
            queue.append(i)
            seq[i] = [1,1]

    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            indegree[nxt] -= 1

            # now에서 순서의 개수가 2개 이상일때
            if seq[now][1] >= 2:
                # now로 nxt 갱신이 가능할 때 
                if seq[nxt][0] < seq[now][0] + 1:
                    seq[nxt] = [seq[now][0]+1,1]
                # now 순서 + 1이 nxt 순서랑 같은 경우
                elif seq[nxt][0] == seq[now][0] + 1:
                    seq[nxt][1] += 1
            else:
                # now로 nxt 갱신이 가능할 때 
                if seq[nxt][0] < seq[now][0]:
                    seq[nxt] = [seq[now][0],1]
                # now 순서 + 1이 nxt 순서랑 같은 경우
                elif seq[nxt][0] == seq[now][0]:
                    seq[nxt][1] += 1


            if indegree[nxt] == 0:
                queue.append(nxt)
                if seq[nxt][1] >= 2:
                    order[nxt] = seq[nxt][0] + 1
                else:
                    order[nxt] = seq[nxt][0]
    
    print(K,order[M])