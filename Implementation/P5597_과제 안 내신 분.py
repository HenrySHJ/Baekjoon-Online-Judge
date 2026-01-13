check = [False]*31

for i in range(28):
    n = int(input())
    check[n] = True

count = 0
for i in range(1,30):
    if count == 2:
        break
    if not check[i]:
        print(i)
        count += 1