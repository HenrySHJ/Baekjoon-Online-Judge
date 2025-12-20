import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# 정렬된 앞뒤 숫자들의 차이들의 최대공약수 찾기 
g = arr[1] - arr[0]
for i in range(2, N):
    g = gcd(g, arr[i]-arr[i-1])

# 최대공약수의 모든 약수 구하기 (2 이상)
ans = set()
for i in range(2, int(g**0.5)+1):
    if g % i == 0:
        ans.add(i)
        ans.add(g//i)

ans.add(g)

print(*sorted(ans))