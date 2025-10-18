import sys
input = sys.stdin.readline

N = int(input())
flowers = []

# 날짜를 MMDD → 정수로 변환해서 다룸
for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    start = sm * 100 + sd
    end = em * 100 + ed
    flowers.append((start, end))

# 시작날짜 기준 정렬, 같으면 끝나는 날짜 긴 순서
flowers.sort(key=lambda x: (x[0], x[1]))

target = 301   # 3월 1일
end_date = 1201  # 12월 1일
cnt = 0
idx = 0
max_end = 0

while target < end_date:
    found = False
    # 현재 target 이전에 피는 꽃 중 가장 오래 가는 꽃 찾기
    while idx < N and flowers[idx][0] <= target:
        if flowers[idx][1] > max_end:
            max_end = flowers[idx][1]
            found = True
        idx += 1
    
    if not found:  # 이어갈 꽃이 없는 경우
        print(0)
        exit()
    
    # 다음 구간으로 이동
    target = max_end
    cnt += 1

print(cnt)