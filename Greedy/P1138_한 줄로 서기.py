import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
ans = [0]*N

for i in range(N):
    j = 0
    count = 0
    while count != A[i]:
        if ans[j] == 0:
            count += 1
        j += 1

    while ans[j] != 0:
        j += 1

    ans[j] = i+1

print(*ans)