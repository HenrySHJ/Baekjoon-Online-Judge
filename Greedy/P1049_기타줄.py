import sys
input = sys.stdin.readline

N,M = map(int,input().split())
six = []
one = []
for _ in range(M):
    a,b = map(int,input().split())
    six.append(a)
    one.append(b)

min_six = min(min(six),min(one)*6)
min_one = min(one)

ans = 0
while N >= 6:
    N -= 6
    ans += min_six

if min_one*N < min_six:
    while N > 0:
        N -= 1
        ans += min_one
else:
    ans += min_six

print(ans)