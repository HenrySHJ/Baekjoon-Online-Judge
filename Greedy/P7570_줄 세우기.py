import sys
input = sys.stdin.readline

N = int(input())
child = [0]+list(map(int,input().split()))

# i가 있는 현재 위치
pos = [0]*(N+1) 

for i in range(1,N+1):
    pos[child[i]] = i

max_len = 1
cur = 1

for i in range(1,N):
    # 연속 값 증가
    if pos[i+1] > pos[i]:
        cur += 1
        max_len = max(max_len, cur)
    # 연속 값 초기화
    else:
        cur = 1

print(N - max_len)