import sys
input = sys.stdin.readline

N = int(input())
N = 1000-N
ans = 0
while N >= 500:
    N -= 500
    ans += 1

while N >= 100:
    N -= 100
    ans += 1

while N >= 50:
    N -= 50
    ans += 1

while N >= 10:
    N -= 10
    ans += 1

while N >= 5:
    N -= 5
    ans += 1

while N >= 1:
    N -= 1
    ans += 1

print(ans)