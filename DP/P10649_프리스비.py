import sys
input = sys.stdin.readline

N,H = map(int,input().split())

cow = []
for _ in range(N):
    h,w,p = map(int,input().split())
    cow.append((h,w,p))
cow.sort(key = lambda x:x[1]+x[2])

# DP[mask] : 비트 상태 mask일때 스택의 안정성
DP = [-1]*(1<<N)
DP[0] = sys.maxsize

# height[mask] : 비트 상태 mask일때 높이
height = [0]*(1<<N)

ans = -1
for mask in range(1<<N):
    # DP 초기화가 이루어지지 않은 부분
    if DP[mask] == -1:
        continue
    
    # 정답 갱신이 가능한 경우
    if height[mask] >= H:
        ans = max(ans, DP[mask])

    for j in range(N):
        # mask에 j 포함되어 있던 경우
        if mask & (1<<j):
            continue

        nmask = mask|(1<<j)

        h,w,p = cow[j]

        # 스택의 안정성 최신화
        np = min(DP[mask]-w, p)

        if np >= 0:
            if np > DP[nmask]:
                DP[nmask] = np
                height[nmask] = height[mask] + h

# 정답 출력
if ans >= 0:
    print(ans)
else:
    print("Mark is too tall")