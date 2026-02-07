import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

l = 0
count = {}
kind = 0
ans = 0

# r 포인터 우로 이동
for r in range(N):
    fruit = S[r]

    # 새로운 과일 정보 추가
    if count.get(fruit, 0) == 0:
        kind += 1
    
    count[fruit] = count.get(fruit, 0) + 1

    # 종류가 두 가지가 넘어가면 l 포인터 우로 이동
    while kind > 2:
        count[S[l]] -= 1

        if count[S[l]] == 0:
            kind -= 1

        l += 1

    ans = max(ans, (r - l + 1))

print(ans)