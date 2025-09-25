import sys
input = sys.stdin.readline

T = int(input())
N = 1000000

# 해당 약수마다 추가시키기
A = [0]*(N+1)
for i in range(1,N+1):
    for j in range(i,N+1,i):
        A[j] += i

S = [0]*(N+1)
for i in range(1,N+1):
    S[i] = S[i-1] + A[i]

out = []
for _ in range(T):
    n = int(input())
    out.append(str(S[n]))

sys.stdout.write("\n".join(out))