import sys
input = sys.stdin.readline

N, X = map(int, input().split())

burger_size = [0]*(N+1)
patties = [0]*(N+1)

burger_size[0] = 1 
patties[0] = 1

# 레별 별 버거 크기 & 패티 크기
for i in range(1, N + 1):
    burger_size[i] = 1 + burger_size[i-1] + 1 + burger_size[i-1] + 1 
    patties[i] = patties[i-1] + 1 + patties[i-1]         

def count_patties(n, x):
    # 레벨 0 : 패티 1개
    if n == 0:
        return 1 if x > 0 else 0
    
    # 맨 밑은 빵
    if x == 1:
        return 0
    
    # 첫 번째 n-1 햄버거 구간
    elif x <= 1 + burger_size[n-1]:
        return count_patties(n-1, x-1)
    
    # 중간 패티 위치일 때
    elif x == 1 + burger_size[n-1] + 1:
        return patties[n-1] + 1
    
    # 두 번째 n-1 햄버거 구간 
    elif x <= 1 + burger_size[n-1] + 1 + burger_size[n-1]:
        # 이전 햄버거 패티 + 중간 패티 + 뒷부분 재귀 탐색
        return patties[n-1] + 1 + count_patties(n-1, x-1-burger_size[n-1]-1)
    
    # 맨 위 빵까지 다 먹었을 때
    else:
        return patties[n]

print(count_patties(N, X))