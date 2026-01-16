import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(now, is_root):
    global count
    dfn[now] = low[now] = count
    count += 1
    
    child_cnt = 0 # DFS 트리에서의 자식 수
    is_articulation = False

    for nxt in graph[now]:
        # 부모 노드로 이동 방지
        if nxt == parent[now]: 
            continue 
        
        # 이미 방문한 노드 (Back-edge)
        if dfn[nxt] != -1: 
            # 방문했던 노드에 대해서 low값 갱신 가능성 확인
            low[now] = min(low[now], dfn[nxt])

        # 미방문 노드 (Tree-edge)
        else:
            child_cnt += 1
            parent[nxt] = now
            DFS(nxt, False)

            #  low[now] = now를 포함하는 서브트리 노드들의 low 값 중 가장 낮은 값
            low[now] = min(low[now], low[nxt])
            
            # 루트가 아니고 nxt가 now보다 위로 못 올라가면 now는 단절점
            if not is_root and low[nxt] >= dfn[now]:
                is_articulation = True
    
    # 루트인 경우 자식 노드가 2개 이상이면 단절점
    if is_root and child_cnt >= 2:
        is_articulation = True
    
    if is_articulation:
        ans.add(now)

V, E = map(int,input().split())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfn = [-1]*(V+1)   # 발견 시점 저장
low = [-1]*(V+1)
parent = [0]*(V+1)
count = 1
ans = set() # 단절점이 중복 저장되는 것 방지

for i in range(1,V+1):
    if dfn[i] == -1:
        DFS(i, True)

result = sorted(list(ans))
print(len(result))
print(*(result))