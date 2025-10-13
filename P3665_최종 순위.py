from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())

    # 작년 순위 (index : 등수, data : 팀 번호)
    last_rank = list(map(int,input().split()))
    last_rank.insert(0,0)

    # 작년 순위 재정렬 (index : 팀 번호, data : 등수)
    last_rank_by_team = [0]*(N+1)
    for i in range(1,N+1):
        last_rank_by_team[last_rank[i]] = i

    M = int(input())
    A = [[] for _ in range(N+1)]  # 인접 그래프
    indegree = [0]*(N+1)  # 진입 차수
    visited = [False]*(N+1)   # 방문 여부

    for _ in range(M):
        a,b = map(int,input().split())
        visited[a] = True
        visited[b] = True

        # 작년에 a가 등수가 더 앞이였다면
        if last_rank_by_team[a] < last_rank_by_team[b]:
            A[b].append(a)
            indegree[a] += 1
            
        # 작년에 b가 등수가 더 앞이였다면
        elif last_rank_by_team[b] < last_rank_by_team[a]:
            A[a].append(b)
            indegree[b] += 1
    
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if last_rank[i] not in A[last_rank[j]]:
                A[last_rank[i]].append(last_rank[j])
                indegree[last_rank[j]] += 1
            
    # 위상 정렬
    queue = deque()
    for i in range(1,N+1):
        if indegree[i] == 0:
            queue.append(i)

    ans = []
    search = True
    while queue:
        # queue에 두 개가 들어오면 순서 설정 불가
        if len(queue) > 1:
            search = False
            break

        now = queue.popleft()
        ans.append(now)
        for next in A[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)
                
    # 정답 출력
    if not search:
        print("?")
    elif len(ans) == N:
        for i in range(len(ans)):
            print(ans[i], end =' ')
        print()
    elif len(ans) < N:
        print("IMPOSSIBLE")