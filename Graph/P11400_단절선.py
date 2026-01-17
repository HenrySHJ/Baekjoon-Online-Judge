import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# DFS Tree 구성 & 단절선 처리
def DFS(now, parent):
    # 발견 순서 & low 값 지정
    global count
    dfn[now] = low[now] = count
    count += 1
    
    for nxt in graph[now]:
        # 부모로 가는 간선 제외
        if nxt == parent: 
            continue 
        
        # 이미 방문한 노드 (우회로)
        if dfn[nxt] != -1: 
            low[now] = min(low[now], dfn[nxt])

        # 미방문 노드
        else: 
            DFS(nxt, now)

            # low 값 갱신
            low[now] = min(low[now], low[nxt])
            
            # 자식이 now 위로 못 올라가는 경우
            if low[nxt] > dfn[now]:
                # 단절선 추가
                bridges.append(tuple(sorted((now, nxt))))

V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfn = [-1]*(V+1)  # 발견시점 저장
low = [-1]*(V+1)  # 이동가능한 가장 낮은 값
count = 1
bridges = []

# 미발견 노드에 대해 DFS
for i in range(1,V+1):
    if dfn[i] == -1:
        DFS(i, 0)

# 정답 출력
bridges.sort()
print(len(bridges))
for b in bridges:
    print(b[0], b[1])