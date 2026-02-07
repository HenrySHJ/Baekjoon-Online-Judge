import sys
input = sys.stdin.readline

N = int(input())
A = [0] * N
B = {}
for i in range(N):
    num = int(input())
    A[i] = num
    B[num] = B.get(num, 0) + 1

A.sort()

print(round(sum(A) / N))
print(A[N // 2])

num = []
num_count = 0
for key in B:
    if num_count < B[key]:
        num_count = B[key]
        num = [key]
    elif num_count == B[key]:
        num.append(key)

num.sort()
if len(num) > 1:
    print(num[1])
else:
    print(num[0])
print(A[-1] - A[0])