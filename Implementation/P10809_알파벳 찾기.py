import sys
input = sys.stdin.readline

S = list(input().strip())

alphabet = [-1]*26

for i in range(len(S)):
    s = S[i]
    if alphabet[ord(s)-97] == -1:
        alphabet[ord(s)-97] = i

print(*alphabet)
