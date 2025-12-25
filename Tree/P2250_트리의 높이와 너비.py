import sys
input = sys.stdin.readline

N = int(input())

left_tree = [0]*(N+1)   # 해당 노드의 왼쪽 자식 노드
right_tree = [0]*(N+1)  # 해당 노드의 오른쪽 자식 노드
parent = [0]*(N+1)

for _ in range(N):
    v,l,r = map(int,input().split())
    if l != -1:
        left_tree[v] = l
        parent[l] = v
    if r != -1:
        right_tree[v] = r
        parent[r] = v

# root 노드 찾기
root = 0
for i in range(1,N+1):
    if parent[i] == 0:
        root = i
        break

depth = [0]*(N+1)
breadth = [0]
max_depth = 0

# 트리 중위 순회하며 너비에 추가
def DFS(now,d):
    global max_depth
    if now == 0:
        return
    
    max_depth = max(max_depth,d)
    depth[now] = d

    left = left_tree[now]
    right = right_tree[now]

    # 중위 순회
    DFS(left,d+1)
    breadth.append(now)
    DFS(right,d+1)

DFS(root,1)

# 해당 레벨의 [최솟값,최댓값]
lvl = [[sys.maxsize,0] for _ in range(max_depth+1)]

for i in range(1,N+1):
    d = depth[breadth[i]]

    lvl[d][0] = min(lvl[d][0],i)
    lvl[d][1] = max(lvl[d][1],i)

idx = root
ans = 0
for i in range(1,max_depth+1):
    if ans < lvl[i][1] - lvl[i][0]:
        idx = i
        ans = lvl[i][1] - lvl[i][0]

print(idx,ans+1)