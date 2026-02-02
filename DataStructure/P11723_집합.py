import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    check = list(input().split())

    if check[0] == 'add':
        if int(check[1]) not in S:
            S.add(int(check[1]))

    elif check[0] == 'remove':
        if int(check[1]) in S:
            S.remove(int(check[1]))

    elif check[0] == 'check':
        if int(check[1]) in S:
            print(1)
        else:
            print(0)

    elif check[0] == 'toggle':
        if int(check[1]) in S:
            S.remove(int(check[1]))
        else:
            S.add(int(check[1]))

    elif check[0] == 'all':
        S = {i for i in range(1,21)}

    elif check[0] == 'empty':
        S = set()