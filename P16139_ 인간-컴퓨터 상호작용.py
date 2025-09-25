import sys
input = sys.stdin.readline

L = input().strip()
Q = int(input())

n = len(L)
# 26개의 prefix sum
S = [[0]*(n+1) for _ in range(26)]

for i in range(n):
    idx = ord(L[i]) - ord('a')
    for j in range(26):
        S[j][i+1] = S[j][i]   # 이전 값 그대로
    S[idx][i+1] += 1          # 해당 문자만 +1

for _ in range(Q):
    a, s, e = input().split()
    a = ord(a) - ord('a')
    s, e = int(s), int(e)
    print(S[a][e+1] - S[a][s])