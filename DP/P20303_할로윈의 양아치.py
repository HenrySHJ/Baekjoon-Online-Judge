import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 그룹 지정 & 그룹별 사탕 개수
def DFS(now,cnt):
    visited[now] = True
    group[now] = cnt
    group_candy[cnt] += C[now]
    group_component[cnt] += 1

    for nxt in friends[now]:
        if not visited[nxt]:
            DFS(nxt,cnt)

N, M, K = map(int, input().split())
C = [0] + list(map(int, input().split()))

# 친구 관계를 인접 리스트로 표현
friends = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

# 묶인 그룹에 따른 번호 지정
group = [0]*(N+1)         # 인원에 따른 그룹 번호
group_cnt = 0             # 그룹 개수
group_candy = [0]         # 그룹별 모든 사탕 개수
group_component = [0]     # 그룹별 구성원 개수
visited = [False]*(N+1)

for i in range(1,N+1):
    if not visited[i]:
        group_cnt += 1
        group_candy.append(0)
        group_component.append(0)
        DFS(i,group_cnt)

# DP[i] : 사탕을 뺏은 인원의 i명일 때 얻을 수 있는 최대 사탕 개수
DP = [0] * K

for i in range(1, group_cnt + 1):
    member = group_component[i] 
    value = group_candy[i]      
    
    for j in range(K - 1, member - 1, -1):
        DP[j] = max(DP[j], DP[j - member] + value)

print(max(DP))