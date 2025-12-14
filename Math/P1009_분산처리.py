import sys
input = sys.stdin.readline

T = int(input())

ans = []
for _ in range(T):
    a,b = map(int,input().split())
    print(pow(a, b, 10) or 10)