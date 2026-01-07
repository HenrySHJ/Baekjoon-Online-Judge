import sys
input = sys.stdin.readline

N = int(input())

line = []
for _ in range(N):
    x,y = map(int,input().split())
    line.append((x,y))

line.sort()

l = line[0][0]
r = line[0][1]

ans = 0
for i in range(1,N):
    nl, nr = line[i]
        
    # 선이 겹치거나 이어지는 경우
    if nl <= r:
        if nr > r:
            r = nr
    # 선이 완전히 끊긴 경우
    else:
        ans += r-l
        l = nl
        r = nr
            
# 마지막 남은 선의 길이 추가
ans += r-l
    
print(ans)