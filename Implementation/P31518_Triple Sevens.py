import sys
input = sys.stdin.readline

N = int(input())

for i in range(3):
    wheel = list(map(int, input().split()))

    check = False
    for j in range(N):
        if wheel[j] == 7:
            check = True
            break

    if not check:
        print(0)
        break
    
    if i == 2:
        print(777)