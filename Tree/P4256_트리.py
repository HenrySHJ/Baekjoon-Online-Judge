import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

T = int(input())

def postOrder_search(start,end):
    global idx
    if start > end:
        return
    
    root = preOrder_list[idx]
    mid = pos[root]
    idx += 1

    postOrder_search(start,mid-1)
    postOrder_search(mid+1,end)
    print(root,end=' ')

for _ in range(T):
    N = int(input())

    preOrder_list = list(map(int,input().split()))
    inOrder_list = list(map(int,input().split()))

    # inOrder에서 노드 위치를 빠르게 찾기 위한 list
    pos = [0]*(N+1)
    for i in range(N):
        pos[inOrder_list[i]] = i

    idx = 0
    postOrder_search(0,N-1)
    print()