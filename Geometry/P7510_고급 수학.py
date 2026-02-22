import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N + 1):
    tri = list(map(int, input().split()))
    tri.sort()

    print("Scenario #" + str(i))

    if tri[2] ** 2 == tri[0] ** 2 + tri[1] ** 2:
        print("yes")

    else:
        print("no")

    if i < N:
        print("")