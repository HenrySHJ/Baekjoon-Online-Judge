T = int(input())

for _ in range(T):
    A = list(input())
    S = []

    for i in A:
        if i == '(':
            S.append(i)
        elif i == ')':
            if S:
                S.pop()
            else:
                S.append(i)
                break

    if S:
        print('NO')
    else:
        print('YES')