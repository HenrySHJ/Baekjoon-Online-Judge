import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
inOrder_list = list(map(int,input().split()))
postOrder_list = list(map(int,input().split()))

tree = []

# inOrder에서 노드 위치를 빠르게 찾기 위한 list
pos = [0]*(N+1)
for i in range(N):
    pos[inOrder_list[i]] = i

post_idx = N-1

ans = []
def preOrder_search(start,end):
    global post_idx
    if start > end:
        return
    
    root = postOrder_list[post_idx]
    post_idx -= 1

    mid = pos[root]

    preOrder_search(mid+1, end)
    preOrder_search(start, mid-1)

    ans.append(root)

preOrder_search(0, N - 1)

for i in range(N-1,-1,-1):
    print(ans[i],end=' ')
