import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
S = int(input())

for i in range(N):
    max_val = -1
    max_idx = -1

    # A[i]를 채울 숫자 찾기
    for j in range(i, min(N,i+S+1)):
        if A[j] > max_val:
            max_val = A[j]
            max_idx = j
            
    # 해당 숫자를 이동
    for j in range(max_idx, i, -1):
        A[j], A[j-1] = A[j-1], A[j]
    
    S -= (max_idx - i)

print(*A)