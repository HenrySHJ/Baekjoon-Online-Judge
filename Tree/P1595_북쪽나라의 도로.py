import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

tree = [[] for _ in range(10001)]

while True:
    try:
        s,e,w = map(int,input().split())
        tree[s].append((e,w))
        tree[e].append((s,w))
    except ValueError or EOFError:
        break

def DFS(node,dist):
    visited[node] = True
    max_dist = dist
    fur_node = node

    for next,weight in tree[node]:
        if not visited[next]:
            n_node,n_dist = DFS(next,dist + weight)

            if n_dist > max_dist:
                max_dist = n_dist
                fur_node = n_node

    return fur_node,max_dist

visited = [False]*10001 
node1,dist = DFS(1,0)

visited = [False]*10001 
node2,ans = DFS(node1,0)

print(ans)