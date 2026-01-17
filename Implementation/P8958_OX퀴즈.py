T = int(input())

for _ in range(T):
    result = list(input())

    ans = 0

    point = 1
    for r in result:
        if r == 'O':
            ans += point
            point += 1

        elif r == 'X':
            point = 1

    print(ans)