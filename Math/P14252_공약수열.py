import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

# 유클리드 호제법
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

ans = 0
for i in range(N-1):
    # 연속된 데이터의 gcd가 1인 구간은 건너뛰기
    if gcd(arr[i],arr[i+1]) == 1:
        continue
    
    for j in range(arr[i]+1,arr[i+1]):
        # 하나의 숫자로 해결이 가능한 경우
        if gcd(arr[i],j) == 1 and gcd(j,arr[i+1]) == 1:
            ans += 1
            break
        # 찾지 못한 경우 2개 더하기
        if j == arr[i+1] - 1: 
            ans += 2

print(ans)