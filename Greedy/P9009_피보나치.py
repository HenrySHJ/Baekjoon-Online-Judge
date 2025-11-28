import sys
input = sys.stdin.readline

T = int(input())

fibo = [0,1]

i = 0
while fibo[i] + fibo[i+1] <= sys.maxsize:
    fibo.append(fibo[i]+fibo[i+1])
    i += 1


for _ in range(T):
    N = int(input())
    ans = []
    i = 1
    while N != 0:
        if fibo[i+1] > N:
            N -= fibo[i]
            ans.append(fibo[i])
            i = 1
        else:
            i += 1

    for i in range(len(ans)-1,-1,-1):
        print(ans[i],end=' ')
    print()