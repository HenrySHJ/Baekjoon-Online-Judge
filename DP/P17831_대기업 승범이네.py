import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

pre = [0,0] + list(map(int,input().split()))

# 사수 정보 바탕으로 인접 그래프 작성
graph = [[] for _ in range(N+1)]
for i in range(2,N+1):
    graph[pre[i]].append(i)

# 각 판매원의 실력 정보
A = [0] + list(map(int,input().split()))

# DP[i] = i번 노드 하위의 다단계에서 [최대 시너지, (0: 멘토링 X, 1: 멘토링 O)]
DP = [[0]*2 for _ in range(N+1)]

# DFS 
def DFS(now):
    for next in graph[now]:
        DFS(next)
        # 현재 정점에서 시너지를 선택하지 않는 경우
        DP[now][0] += max(DP[next][0],DP[next][1])

    # 현재 정점에서 시너지를 선택하는 경우
    for next in graph[now]:
        DP[now][1] = max(DP[now][1], DP[now][0]-max(DP[next])+DP[next][0]+A[now]*A[next])

DFS(1)

print(max(DP[1]))