import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())

city = [list(map(int,input().split())) for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

min_city_distance = sys.maxsize

# 치킨 집 중 M개 고르는 조합 모두 탐색하기
for selected_chicken in combinations(chicken, M):
    total_distance = 0
    
    # 집 h의 치킨 거리 구하기
    for h in house:
        temp_distance = sys.maxsize
        for c in selected_chicken:
            dist = abs(h[0]-c[0]) + abs(h[1]-c[1])
            if dist < temp_distance:
                temp_distance = dist
        
        total_distance += temp_distance
    
    if total_distance < min_city_distance:
        min_city_distance = total_distance

print(min_city_distance)