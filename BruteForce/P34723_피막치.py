import sys
input = sys.stdin.readline

P,M,C = map(int,input().split())
X = int(input())

ans = sys.maxsize
for i in range(1,P+1):
    for j in range(1,M+1):
        for k in range(1,C+1):
            ans = min(ans,abs((i+j)*(j+k)-X))

print(ans)