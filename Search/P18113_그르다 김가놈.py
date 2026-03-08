import sys
input = sys.stdin.readline

N, K, M = map(int, input().split())

kimbap = []
for _ in range(N):
    l = int(input())

    if l >= 2 * K:
        cut = l - 2 * K
        if cut > 0: 
            kimbap.append(cut)

    elif l > K:
        cut = l - K
        if cut > 0: 
            kimbap.append(cut)

if not kimbap:
    print(-1)
    sys.exit()

start = 1
end = max(kimbap)
ans = -1

# 자를 길이 P에 대해서 이분 탐색
while start <= end:
    mid = (start + end) // 2

    count = 0
    for kb in kimbap:
        count += (kb // mid)

        if count >= M:
            break

    if count >= M:
        ans = mid
        start = mid + 1

    else:
        end = mid - 1

print(ans)