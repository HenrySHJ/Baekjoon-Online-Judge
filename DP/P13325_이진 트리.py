import sys
input = sys.stdin.readline

K = int(input())
w = list(map(int, input().split()))

# 노드 개수: 2**(K+1)
N = 1 << (K + 1)

# 가중치 배열 (root:0)
arr = [0]*N
for i in range(2,N):
    arr[i] = w[i-2]

# DP[i]: i에서 리프까지의 최대 경로 합
DP = [0]*N 
ans = 0

# 아래에서 위로
for i in range((N//2)-1,0,-1):
    left = DP[i*2] + arr[i*2]
    right = DP[i*2+1] + arr[i*2+1]

    ans += abs(left-right)
    DP[i] = max(left, right)

# 초기 가중치 합 + 증가분
print(sum(arr) + ans)