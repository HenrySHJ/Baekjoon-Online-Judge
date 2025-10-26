import sys
input = sys.stdin.readline

N,Q = map(int,input().split())

A = list(map(int,input().split()))
length = len(A)

tree = [0]*(4*N)

# tree에 노드 채우기
def build(node,start,end):
    if start == end:
        tree[node] = A[start]
        return

    mid = (start + end) // 2 
    build(node*2, start, mid)
    build(node*2 + 1, mid + 1, end)

    tree[node] = tree[node*2] + tree[node*2 + 1]
    
build(1,0,length - 1)

# 출력 처리
def query(node,start,end,l,r):
    if start > r or end < l:
        return 0
    
    if start >= l and end <= r:
        return tree[node]
    
    mid = (start + end) // 2

    return query(node*2,start,mid,l,r) + query(node*2+1,mid+1,end,l,r)

# 노드 바꾼 후 tree 처리
def change(node,start,end,a,b):
    if start > a or end < a:
        return

    if start == end and start == a:
        tree[node] = b
        return
    
    mid = (start + end) // 2

    change(node*2,start,mid,a,b)
    change(node*2 + 1,mid+1,end,a,b)

    tree[node] = tree[node*2] + tree[node*2 + 1]

for _ in range(Q):
    x,y,a,b = map(int,input().split())
    ny = max(x,y)
    nx = min(x,y)
    print(query(1,0,length-1,nx-1,ny-1))
    change(1,0,length-1,a-1,b)