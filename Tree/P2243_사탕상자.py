import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

MAX_NUM = 1000000
tree = [0]*(4*MAX_NUM)

# 사탕을 상자에 넣거나 빼기
def update(node,start,end,target,count):
    if start == end:
        tree[node] += count
        return 
    
    mid = (start + end) // 2

    if target <= mid:
        update(node*2,start,mid,target,count)
    else:
        update(node*2+1,mid+1,end,target,count)
    
    tree[node] = tree[node*2] + tree[node*2+1]

def search(node,start,end,rank):
    if start == end:
        return start
    
    mid = (start + end) // 2

    if rank <= tree[node*2]:
        return search(node*2,start,mid,rank)
    else:
        return search(node*2+1,mid+1,end,rank-tree[node*2])

for _ in range(N):
    query = list(map(int,input().split()))

    if query[0] == 1:
        B = query[1]
        candy = search(1,1,MAX_NUM,B)
        print(candy)

        update(1,1,MAX_NUM,candy,-1)

    elif query[0] == 2:
        B,C = query[1], query[2]
        update(1,1,MAX_NUM,B,C)