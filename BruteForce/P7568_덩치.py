import sys
input = sys.stdin.readline

N = int(input())

person = [tuple(map(int, input().split())) for _ in range(N)]
rank = [0] * N

for i in range(N):
    rank_i = 1
    for j in range(N):
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            rank_i += 1
    rank[i] = rank_i

print(*rank)