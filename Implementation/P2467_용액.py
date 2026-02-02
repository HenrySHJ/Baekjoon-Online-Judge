import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 경계선 잡기
p1 = 0
p2 = N - 1

ans = sys.maxsize
ans_left = 0
ans_right = 0

while p1 < p2:
    cur = A[p1] + A[p2]

    # 정답 갱신
    if abs(cur) < ans:
        ans = abs(cur)
        ans_left = A[p1]
        ans_right = A[p2]
        
    # 합이 0이면  종료
    if cur == 0:
        break
    
    # 합이 0보다 크면 큰 값을 줄이기
    if cur > 0:
        p2 -= 1
    # 합이 0보다 작으면 작은 값을 키우기
    else:
        p1 += 1

print(ans_left, ans_right)