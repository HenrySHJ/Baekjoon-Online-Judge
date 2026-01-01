import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    V,E = map(int,input().split())

    print(E-V-2)