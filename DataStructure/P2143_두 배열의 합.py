import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

# A의 모든 부분합 
sum_a = []
for i in range(N):
    cur_sum = 0
    for j in range(i, N):
        cur_sum += A[j]
        sum_a.append(cur_sum)
            
# B의 모든 부분합 
sum_b = []
for i in range(M):
    cur_sum = 0
    for j in range(i, M):
        cur_sum += B[j]
        sum_b.append(cur_sum)

count_b = Counter(sum_b)
    
# A의 부분합 확인하기
ans = 0
for sa in sum_a:
    target = T - sa
    
    if target in count_b:
        ans += count_b[target]

print(ans)