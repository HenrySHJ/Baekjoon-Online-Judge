import sys
input = sys.stdin.readline

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
A,B = map(int,input().split())

# 정답이 되는 두 수의 곱
# A : gcd(a,b) / B : a*b // gcd(a,b)
mul = A*B

ans = [1,mul]
for i in range(2,int(mul**0.5)+1):
    # mul의 약수가 아니면 건너뛰기
    if mul % i != 0:
        continue
    
    # 최대공약수가 다른 수면 건너뛰기
    if gcd(i,mul//i) != A:
        continue

    # 합이 더 작으면 갱신
    if i + (mul // i) < sum(ans):
        ans[0] = i
        ans[1] = mul // i

print(*ans)