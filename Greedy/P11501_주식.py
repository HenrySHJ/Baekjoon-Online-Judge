import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    cost = list(map(int,input().split()))

    ans = 0
    max_cost = 0
    for i in range(N-1,-1,-1):
        if cost[i] > max_cost:
            max_cost = cost[i]
        else:
            ans += max_cost - cost[i]

    print(ans)