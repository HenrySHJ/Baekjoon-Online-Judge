import sys
input = sys.stdin.readline

S = list(input().strip())
A = B = 0
if S[0] == '1':
    A += 1
else:
    B += 1

for i in range(len(S)-1):
    if S[i] == S[i+1]:
        continue
    else:
        if S[i+1] == '1':
            A += 1
        else:
            B += 1

print(min(A,B))