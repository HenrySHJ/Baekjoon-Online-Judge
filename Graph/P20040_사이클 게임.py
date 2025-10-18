import sys
input = sys.stdin.readline

N,M = map(int,input().split())

parent = [[] for _ in range(N)]

for i in range(N):
    parent[i] = i

# 유니온-파인드
def find(a):
    while a != parent[a]:
        parent[a] = parent[parent[a]]  # 경로 압축
        a = parent[a]
    return a
    
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for i in range(M):
    a,b = map(int,input().split())
    # union(a,b)을 시도했을 때 이미 a,b의 parent가 같다면 break
    if find(a) == find(b):
        print(i+1)
        break
    union(a,b)
    # 없을 시 0 출력
    if i == M-1:
        print(0)