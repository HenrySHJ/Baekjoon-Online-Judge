import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N = int(input())

    closet = {}
    
    for _ in range(N):
        clothes, type = input().split()

        if closet.get(type, 0) == 0:
            closet[type] = [clothes]
        else:
            closet[type].append(clothes)

    ans = 1
    for key in closet:
        ans *= len(closet[key]) + 1

    ans -= 1
    print(ans)