import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

tree = [[] for _ in range(N+1)]

# 그래프 인접 리스트 + 가중치
for i in range(N-1):
    s,e,w = map(int,input().split())
    tree[s].append((e,w))
    tree[e].append((s,w))

# DFS + 최소거리
def DFS(now,dist):
    visited[now] = True
    max_dist = dist
    furthest = now

    for next,weight in tree[now]:
        if not visited[next]:
            new_now,new_dist = DFS(next,dist+weight)
        
            if new_dist > max_dist:
                max_dist = new_dist
                furthest = new_now

    return furthest,max_dist

# 루트 노드로부터 최대거리 찾기
visited = [False]*(N+1)
node,d = DFS(1,0)

# 최대거리의 노드로부터 최대거리 찾기
visited = [False]*(N+1)
d, ans = DFS(node,0)

print(ans)