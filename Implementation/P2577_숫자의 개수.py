A = int(input())
B = int(input())
C = int(input())

D = A*B*C

check = [0]*10
lst = list(str(D))

for l in lst:
    check[int(l)] += 1

for i in range(10):
    print(check[i])