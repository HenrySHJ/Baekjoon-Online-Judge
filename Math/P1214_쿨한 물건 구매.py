import sys
input = sys.stdin.readline

D, P, Q = map(int, input().split())

# P를 더 큰 수로 설정
if P < Q:
    P, Q = Q, P

count_p = 1
count_q = 0

ans = sys.maxsize

while count_p > 0:
    # 현재 가격이 목표 가격보다 작으면 p 개수 + 1
    if count_p * P + count_q * Q < D:
        count_p += 1

    else:
        ans = min(ans, count_p * P + count_q * Q)
        if ans == D:
            break

        count_p -= 1
        count_q += 1

        while count_p * P + count_q * Q < D:
            count_q += 1

        ans = min(ans, count_p * P + count_q * Q)
        if ans == D:
            break

print(ans)