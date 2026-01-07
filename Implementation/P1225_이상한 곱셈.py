A,B = input().split()

ans = 0
for a in A:
    for b in B:
        ans += int(a)*int(b)

print(ans)