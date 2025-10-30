import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())


A = [list(map(int,input().split())) for _ in range(N)]
DP = [[0]*N for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def DFS(x, y):
    # 계산된 경우는 1 이상으로 처리 예정
    if DP[x][y] != 0:
        return DP[x][y]
    
    # 자기 자신
    DP[x][y] = 1
    
    # 상하좌우 체크
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 범위 유효성 검사 & 대나무 개수 증가 검사
        if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > A[x][y]:
            DP[x][y] = max(DP[x][y], DFS(nx, ny) + 1)
    
    return DP[x][y]

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, DFS(i, j))

print(ans)