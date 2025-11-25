import sys
input = sys.stdin.readline

N = int(input())

dist = list(map(int,input().split()))
cost = list(map(int,input().split()))

min_cost = cost[0]
answer = 0

for i in range(N-1):
    min_cost = min(min_cost, cost[i])
    answer += min_cost * dist[i]

print(answer)