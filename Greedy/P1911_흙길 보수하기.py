import sys
input = sys.stdin.readline

N, L = map(int, input().split())
puddles = []
for _ in range(N):
    puddles.append(list(map(int,input().split())))
    
puddles.sort()
    
ans = 0

# 현재 널빤지 마지막 위치
cur = 0
    
for start, end in puddles:
    # 널빤지가 이미 이 웅덩이의 끝보다 멀리 가 있는 경우
    if cur > end:
        continue
        
    # 비교 지점으로 cur이랑 start 중 더 큰 좌표 선택
    if cur < start:
        cur = start
            
    # 남은 웅덩이 길이를 덮기 위해 필요한 널빤지 수 계산
    dist = end - cur
    if dist <= 0:
        continue
            
    # 필요한 개수
    count = (dist+L-1)//L
        
    ans += count
    cur += count*L
        
print(ans)