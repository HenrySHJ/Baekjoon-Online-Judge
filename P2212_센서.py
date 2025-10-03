N = int(input())
K = int(input())

A = list(map(int,input().split()))
A.sort()

# dist : 앞 인덱스 값와의 차
dist = [0]*len(A)
dist[0] = 0

for i in range(1,len(A)):
    dist[i] = A[i] - A[i-1]
dist.sort()

# S중 K-1개 만큼 최댓값을 덜어내기
for _ in range(K-1):
    if dist:
        dist.pop()

ans = 0
for i in range(len(dist)):
    ans += dist[i]

print(ans)