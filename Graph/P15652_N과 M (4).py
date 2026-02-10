N, M = map(int ,input().split())

def DFS(length):
    if length == M:
        print(*ans)
        return
    
    
    for nxt in range(1, N + 1):
        if ans:
            if ans[-1] <= nxt:
                ans.append(nxt)
                DFS(length + 1)
                ans.pop()
        else:
            ans.append(nxt)
            DFS(length + 1)
            ans.pop()

ans = []
DFS(0)