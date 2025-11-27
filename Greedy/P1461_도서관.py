import sys
input = sys.stdin.readline

N,M = map(int,input().split())

book = list(map(int,input().split()))

# 음수와 양수로 분리
plus = []
minus = []

for i in range(N):
    if book[i] < 0:
        minus.append(book[i])
    else:
        plus.append(book[i])

plus.sort()
minus.sort()

ans = []
for i in range(len(plus)-1,-1,-M):
    ans.append(plus[i])

for i in range(0,len(minus),M):
    ans.append(abs(minus[i]))

print(sum(ans)*2-max(ans))