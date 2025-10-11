N,M,K = map(int,input().split())
price = list(map(int,input().split()))
price.insert(0,0)

visited = [False]*(N+1)
parent = [0 for _ in range(N+1)]
for i in range(1,N+1):
    parent[i] = i

# 유니온 파인드
def find(a):
    while a != parent[a]:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

# 저렴한 친구를 부모로 만들기
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        if price[a] > price[b]:
            parent[a] = b
        else:
            parent[b] = a

for _ in range(M):
    a,b = map(int,input().split())
    union(a,b)

# 미방문 그룹의 금액을 ans에 더하기
ans = 0
for i in range(1,N+1):
    anc = find(i)
    if not visited[anc]:
        visited[anc] = True
        ans += price[anc]

# 최종 금액 판별
if K >= ans:
    print(ans)
else:
    print("Oh no")