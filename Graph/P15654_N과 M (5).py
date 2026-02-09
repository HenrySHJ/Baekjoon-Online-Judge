import sys
input = sys.stdin.readline

def DFS(depth):
    if depth == M:
        print(*ans)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            ans.append(nums[i])
            
            DFS(depth + 1)
            
            # 백트래킹
            ans.pop()
            visited[i] = False

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

visited = [False] * N
ans = []
DFS(0)