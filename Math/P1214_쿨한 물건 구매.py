import sys
input = sys.stdin.readline

D, P ,Q = map(int, input().split())

# P를 더 큰 값으로 두기
if Q > P:
    Q, P = P, Q

# ans 초기값: P로만 샀을 때 vs Q로만 샀을 때 중 작은 값
only_P = ((D + P - 1) // P) * P
only_Q = ((D + Q - 1) // Q) * Q
ans = min(only_P, only_Q)

# P를 i개 샀을 때의 최소 금액 탐색
for i in range(1, min(D // P, Q) + 1):
    # P를 i개 쓰고 남은 목표 금액
    rem = D - P * i

    # Q로 남은 금액을 채우기
    ans = min(ans, ((rem + Q - 1) // Q) * Q + P * i)

print(ans)