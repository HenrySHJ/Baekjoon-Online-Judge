import sys
input = sys.stdin.readline

N = int(input())

S = [list(input().strip()) for _ in range(N)]
len_file = len(S[0])

ans = ''
for i in range(len_file):
    check = True
    for j in range(N-1):
        if S[j][i] != S[j+1][i]:
            check = False
            break

    if check:
        ans += str(S[0][i])
    else:
        ans += '?'

print(ans)