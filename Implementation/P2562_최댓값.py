num = [int(input()) for _ in range(9)]

ans = 0
idx = -1
for i in range(9):
    if ans < num[i]:
        ans = num[i]
        idx = i
print(ans)
print(idx+1)