while True:
    N = list(input())

    if len(N) == 1 and N[0] == '0':
        break

    check = 'yes'
    for i in range(len(N)//2+1):
        if N[i] != N[-i-1]:
            check = 'no'

    print(check)