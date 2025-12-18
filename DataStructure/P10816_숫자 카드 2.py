import sys
import bisect
input = sys.stdin.readline

N = int(input())
cards = list(map(int,input().split()))
cards.sort()

M = int(input())
query = list(map(int,input().split()))

for q in query:
    print(bisect.bisect_right(cards, q) - bisect.bisect_left(cards, q),end=' ')