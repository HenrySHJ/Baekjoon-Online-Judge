N = int(input())

temp = N
ans = 0
while ans == 0 or temp != N:
    a = temp // 10
    b = temp % 10

    c = (a + b) % 10

    temp = b*10 + c
    ans += 1

print(ans)