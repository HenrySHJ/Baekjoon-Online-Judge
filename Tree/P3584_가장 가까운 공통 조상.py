import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def BFS(node):
    queue = deque()
    queue.append(node)
    while queue:
        now_node = queue.popleft()
        for next in tree[now_node]:
            queue.append(next)
            parent[next] = now_node
            depth[next] = depth[now_node] + 1

def executeLCA(a,b):
    if depth[a] < depth[b]:
        temp = b
        b = a
        a = temp

    while depth[a] != depth[b]:
        a = parent[a]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a


for _ in range(T):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    check = [[] for _ in range(N+1)]
    visited = [False]*(N+1)
    depth = [0]*(N+1)
    parent = [0]*(N+1)

    # 인접 리스트
    for _ in range(N-1):
        A,B = map(int,input().split())
        tree[A].append(B)
        check[B].append(A)

    # 루트 노드의 인덱스 찾기
    root = 1
    while root <= N:
        if len(check[root]) == 0:
            break
        else:
            root += 1

    BFS(root)

    a,b = map(int,input().split())
    print(executeLCA(a,b))