import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    word = input().strip()
    print(word[0] + word[-1])