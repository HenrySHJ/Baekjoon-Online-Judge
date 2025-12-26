import sys
input = sys.stdin.readline

tree = [i for i in range(1024)]

T = int(input())

for _ in range(T):
    a,b = map(int,input().split())

    while a != b:
        if a > b:
            a //= 2
        else:
            b //= 2
        
    print(a*10)