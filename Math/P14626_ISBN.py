code = list(input())

total = 0
mul = 0
for i in range(13):
    if code[i] != "*":
        if i % 2 == 0:
            total += int(code[i])
        else:
            total += int(code[i]) * 3
    else:
        if i % 2 == 0:
            mul = 1
        else:
            mul = 3

for x in range(10):
    if (total + (x * mul)) % 10 == 0:
        print(x)
        break