import sys
import math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a,b = map(int,input().split())

    dist = b - a 

    # 제곱수에서 새로운 광년 비행
    n = int(math.sqrt(dist))
        
    if n**2 == dist:
        print(2*n-1)

    elif dist <= n**2+n:
        print(2*n)

    else:
        print(2*n+1)
    