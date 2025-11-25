import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]

weight = {}

# 단어마다 자릿수에 따른 가중치 부여
for w in words:
    p = 1
    for alphabet in reversed(w):
        weight[alphabet] = weight.get(alphabet, 0) + p
        p *= 10

weights = sorted(weight.values(), reverse=True)

num = 9
answer = 0
for w in weights:
    answer += w*num
    num -= 1

print(answer)