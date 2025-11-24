import sys,heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    rank = []

    for _ in range(N):
        a,b = map(int,input().split())
        rank.append((a,b))

    rank.sort(key=lambda x:x[0])

    ans = 1
    min_b = rank[0][1]
    for i in range(len(rank)-1):
        if min_b > rank[i+1][1]:
            min_b = rank[i+1][1]
            ans += 1
    
    print(ans)
