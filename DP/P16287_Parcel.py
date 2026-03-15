import sys
input = sys.stdin.readline

W, N = map(int, input().split())
A = list(map(int, input().split()))

DP = [False] * (W + 1)

for i in range(N):
    # i 이후의 수를 더해서 합 구하기
    for j in range(i + 1, N):
        cur = A[i] + A[j]
        
        # 합이 W가 되는 수 존재하면
        if cur <= W and DP[W - cur]:
            print("YES")
            sys.exit()
    
    # i 이전의 수를 더해서 합 구하기 (겹치기 방지)
    for k in range(i):
        prev = A[i] + A[k]
        if prev <= W:
            DP[prev] = True
                
print("NO")