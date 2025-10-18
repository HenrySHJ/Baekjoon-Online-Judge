from collections import deque

N = int(input())

time = [0]*(N+1)  # 작업 소요 시간
A = [[] for _ in range(N+1)]  # 인접 리스트
indegree = [0]*(N+1)  # 진입 차수
dp = [0]*(N+1)  # 각 작업의 완료 시간

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]

    for j in range(2, len(temp)):
        A[temp[j]].append(i)
        indegree[i] += 1

queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = time[i]  # 자기 자신 완료 시간

while queue:
    now = queue.popleft()
    for next in A[now]:
        indegree[next] -= 1
        dp[next] = max(dp[next], dp[now] + time[next])
        if indegree[next] == 0:
            queue.append(next)

print(max(dp))  # 전체 중 가장 오래 걸린 시간