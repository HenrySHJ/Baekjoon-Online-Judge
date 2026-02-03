import sys

N = int(input())

for i in range(1, N + 1):
    ans = i + sum(map(int, str(i)))
    
    if ans == N:
        print(i)
        sys.exit()

print(0)