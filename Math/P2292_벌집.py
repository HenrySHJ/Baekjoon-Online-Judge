N = int(input())

S = 1
k = 1
while N > S:
    S = S + k * 6
    k += 1

print(k)