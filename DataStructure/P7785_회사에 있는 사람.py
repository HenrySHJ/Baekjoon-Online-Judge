import sys
input = sys.stdin.readline

N = int(input())

log = {}

for _ in range(N):
    name, act = input().split()
    if act == 'enter':
        log[name] = log.get(name,0) + 1
    elif act == 'leave':
        log.pop(name)

list_log = reversed(sorted(log.keys()))

for name in list_log:
    print(name)