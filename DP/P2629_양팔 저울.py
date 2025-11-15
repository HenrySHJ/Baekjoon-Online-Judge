import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int,input().split()))

M = int(input())
check = list(map(int,input().split()))

MAX = 15000  # 30개 * 500g
DP = [False]*(MAX+1)
DP[0] = True

for c in weights:
    # 연산 중복 방지 위한 임시 DP
    temp = DP[:]  

    for w in range(MAX + 1):
        if DP[w]:
            if w + c <= MAX:
                temp[w + c] = True
            temp[abs(w - c)] = True

    DP = temp

for i in check:
    if i <= MAX and DP[i]:
        print("Y", end=' ')
    else:
        print("N", end=' ')