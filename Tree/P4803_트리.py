import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def find(a):
    while a != parent[a]:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        # 서로 다른 집합일때 
        parent[b] = a
        if not is_tree[b]:
            is_tree[a] = False
    else:
        # 이미 같은 집합인데 또 연결됨 = 사이클 발생
        is_tree[a] = False

case_count = 1
while True:
    N,M = map(int,input().split())
    
    if N == 0 and M == 0:
        break
    
    parent = [i for i in range(N+1)]    
    is_tree = [True]*(N+1)
    for _ in range(M):
        u,v = map(int,input().split())
        union(u,v)

    T = 0
    for i in range(1, N+1):
        # i가 자기 자신의 부모이면서, 트리 상태가 True인 것만 카운트
        if parent[i] == i and is_tree[i]:
            T += 1
    
    if T > 1:
        print("Case "+str(case_count)+": A forest of "+str(T)+" trees.")
    elif T == 1:
        print("Case "+str(case_count)+": There is one tree.")
    else:
        print("Case "+str(case_count)+": No trees.")

    case_count += 1