import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

G = int(input())
P = int(input())

# 부모 게이트 초기화
parent = [i for i in range(G+1)]

# 유니온-파인드
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # 경로 압축
        x = parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    parent[a] = b

ans = 0
for _ in range(P):
    g = int(input())
    dock = find(g)
    if dock == 0:   # 더 이상 도킹할 수 없는 경우
        break
    ans += 1
    union(dock, dock-1)  # dock 게이트를 사용했으니 dock-1로 연결

print(ans)