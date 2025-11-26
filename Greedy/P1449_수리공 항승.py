import sys
input = sys.stdin.readline

N,L = map(int,input().split())
leak = list(map(int,input().split()))
leak.sort()
taped = [False]*N

ans = 0
for i in range(N):
    if taped[i]:
        continue
    
    ans += 1
    for j in range(i+1,N):
        if leak[j] - leak[i] + 1 <= L:
            taped[j] = True
        else:
            break

print(ans)