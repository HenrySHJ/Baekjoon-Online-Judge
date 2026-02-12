import sys
input = sys.stdin.readline

N = int(input())

sell = {}

for _ in range(N):
    name = input().strip()
    sell[name] = sell.get(name, 0) + 1

ans = ""
val = 0
for key in sell:
    if val < sell[key]:
        val = sell[key]
        ans = key

    elif val == sell[key]:
        if ans > key:
            ans = key

print(ans)