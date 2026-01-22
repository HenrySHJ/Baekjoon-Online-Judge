import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
A = list(map(int,input().split()))

tree = [0]*(4*N)

def build(node,start,end):
    if start == end:
        tree[node] = A[start]
        return
    
    mid = (start + end) // 2

    build(node*2,start,mid)
    build(node*2+1,mid+1,end)

    tree[node] = min(tree[node*2],tree[node*2+1])

def update(node,start,end,target,val):
    if start == end:
        tree[node] = val
        return
    
    mid  = (start + end) // 2

    if target <= mid:
        update(node*2,start,mid,target,val)
    else:
        update(node*2+1,mid+1,end,target,val)

    tree[node] = min(tree[node*2],tree[node*2+1])

def query(node,start,end,left,right):
    if start > right or end < left:
        return sys.maxsize

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2

    return min(query(node*2,start,mid,left,right),query(node*2+1,mid+1,end,left,right))    

M = int(input())

build(1,0,N-1)
for _ in range(M):
    q = list(map(int,input().split()))
    if q[0] == 1:
        i,v = q[1],q[2]
        update(1,0,N-1,i-1,v)

    elif q[0] == 2:
        i,j = q[1],q[2]
        ans = query(1,0,N-1,i-1,j-1)
        print(ans)