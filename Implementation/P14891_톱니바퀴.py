import sys
from collections import deque
input = sys.stdin.readline

gear = [deque(list(input().strip())) for _ in range(4)]

K = int(input())

for _ in range(K):
    num, direct = map(int, input().split())
    num -= 1  
    
    # 각 바퀴의 회전 방향 저장
    move = [0]*4
    move[num] = direct
    
    # 오른쪽 방향
    for i in range(num, 3):
        if gear[i][2] != gear[i+1][6]:
            move[i+1] = -move[i]
        else:
            break
            
    # 왼쪽 방향
    for i in range(num, 0,-1):
        if gear[i][6] != gear[i-1][2]:
            move[i-1] = -move[i]
        else:
            break
            
    # 결정된 방향대로 덱 연산
    for i in range(4):
        if move[i] == 1:
            gear[i].appendleft(gear[i].pop())
        elif move[i] == -1:
            gear[i].append(gear[i].popleft())
            

# 점수 계산
ans = 0
for i in range(4):
    if gear[i][0] == '1':
        ans += 2**i

print(ans)