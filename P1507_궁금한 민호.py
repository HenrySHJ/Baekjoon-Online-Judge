import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 일관성 검증
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or i == k or j == k:
                continue
            # 최단 거리 행렬이 모순되면 바로 종료
            if A[i][j] > A[i][k] + A[k][j]:
                print(-1)
                sys.exit()

# 불필요한 간선 제거 후 필요한 간선 합 계산
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        check = True
        for k in range(N):
            if k != i and k != j and A[i][j] == A[i][k] + A[k][j]:
                check = False
                break
        if check:
            ans += A[i][j]

print(ans)