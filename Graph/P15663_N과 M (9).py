import sys
input = sys.stdin.readline

def DFS(depth):

    # 길이가 M이 되면 출력
    if depth == M:
        print(*ans)
        return

    lastNum = -1

    for i in range(N):
        if visited[i]:
            continue
        
        if nums[i] == lastNum:
            continue

        visited[i] = True
        ans.append(nums[i])
        lastNum = nums[i]

        DFS(depth + 1)

        # 백트래킹
        ans.pop()
        visited[i] = False

N, M = map(int, input().split())
nums = list(map(int ,input().split()))
nums.sort()

visited = [False] * N
ans = []
DFS(0)