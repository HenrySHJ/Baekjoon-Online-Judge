import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())

boxes = []
for _ in range(M):
    s, e, cnt = map(int, input().split())
    boxes.append((e, s, cnt))

# 도착지 기준 정렬
boxes.sort()

ans = 0
truck = [0] * (N+1)  # 1~N 마을 사이 구간의 현재 적재량

for e, s, cnt in boxes:
    # s ~ e-1 구간에서 남은 용량 확인
    max_load = cnt
    # 적재해서 C 넘으면 그 양만큼 max_load 줄이기
    for i in range(s, e):
        max_load = min(max_load, C - truck[i])
    
    # 싣을 수 있는 만큼 싣기
    if max_load > 0:
        for i in range(s, e):
            truck[i] += max_load
        ans += max_load

print(ans)