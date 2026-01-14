import sys
input = sys.stdin.readline

N,M = map(int,input().split())

name_book = ['']*(N+1)
num_book = {}

for i in range(N):
    name = input().strip()
    name_book[i+1] = name
    num_book[name] = num_book.get(name,0) + i+1

for _ in range(M):
    m = input().strip()
    try:
        if type(int(m)) == int:
            print(name_book[int(m)])
    except ValueError:
        print(num_book[m])