N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

def DFS(length):
    if length == M:
        print(*ans)
        return

    lastnum = -1

    for nxt in A:
        if ans:
            if ans[-1] <= nxt and nxt != lastnum:
                ans.append(nxt)
                lastnum = nxt

                DFS(length + 1)
                ans.pop()
        else:
            if nxt != lastnum:
                ans.append(nxt)
                lastnum = nxt

                DFS(length + 1)
                ans.pop()

ans = []
DFS(0)