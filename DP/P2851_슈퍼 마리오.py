import sys
input = sys.stdin.readline

mush = [int(input()) for _ in range(10)]

ans = 0
S = 0

for x in mush:
    S += x
    if abs(S - 100) < abs(ans - 100):
        ans = S
    elif abs(S - 100) == abs(ans - 100) and S > ans:
        ans = S

print(ans)