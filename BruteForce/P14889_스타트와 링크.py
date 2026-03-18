import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ans = sys.maxsize

# True면 스타트 팀
visited = [False] * N
ans = sys.maxsize

# DFS + 백트래킹
def DFS(now, count):
    global ans
    
    # 스타트 팀 채워짐 -> 나머지는 자연스럽게 링크 팀
    if count == N // 2:
        team_start = 0
        team_link = 0
        
        # 같은 팀에 속한 경우 시너지 점수 계산
        for i in range(N):
            for j in range(i + 1, N):
                # 같은 팀에 속한 경우
                if visited[i] and visited[j]:
                    team_start += A[i][j] + A[j][i]
                
                # 둘 다 반대 팀인 경우
                elif not visited[i] and not visited[j]:
                    team_link += A[i][j] + A[j][i]
        
        # 시너지 점수 갱신 여부 확인
        ans = min(ans, abs(team_start - team_link))
        return

    # 재귀 & 백트래킹
    for i in range(now, N):
        # 아직 팀 배정이 안됐다면 스타트팀
        if not visited[i]:
            visited[i] = True

            # 다음 인원 탐색
            DFS(i + 1, count + 1) 

            # 스타트 팀에서 빼기
            visited[i] = False     

DFS(0, 0)
print(ans)