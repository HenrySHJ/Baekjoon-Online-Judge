import sys
input = sys.stdin.readline

a,b = map(int,input().split())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

ans1 = gcd(a,b)
print(ans1)
print(a*b//ans1)