import sys
input = sys.stdin.readline

N = list(input().strip())

zero = False
total = 0
for i in range(len(N)):
    if N[i] == '0':
        zero = True

    total += int(N[i])

if total % 3 == 0 and zero:
    N.sort(reverse=True)

    ans = 0
    for i in range(len(N)):
        ans = ans*10 + int(N[i])

    print(ans)
else:
    print(-1)