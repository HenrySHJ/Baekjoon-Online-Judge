import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
A = list(map(int,input().split()))

tree = [None]*(4*N)

# 상위 노드 채우기
def check(a,b):
    # 값이 작은 인덱스가 상위 노드에 저장
    if a[0] < b[0]:
        return a
    if a[0] > b[0]:
        return b
    
    # 값이 같으면 인덱스 순
    return a if a[1] < b[1] else b

# 트리에 (노드,인덱스) 구조로 저장
def build(node,start,end):

    if start == end:
        tree[node] = (A[start],start)
        return
    mid = (start+end) // 2

    build(node*2,start,mid)
    build(node*2+1,mid+1,end)

    tree[node] = check(tree[node*2],tree[node*2 + 1])

build(1,0,N-1)

# 1번 쿼리 : 세그먼트 트리 값 바꾸기
def change(node,start,end,i,v):
    # (노드,인덱스) 형태로 저장
    if start == end:
        tree[node] = (v,i)
        A[i] = v
        return
    
    mid = (start + end) // 2
    if i <= mid:
        change(node*2, start, mid, i, v)
    else:
        change(node*2+1, mid+1, end, i, v)

    tree[node] = check(tree[node*2], tree[node*2+1])

# 2번 쿼리 : i~j중 최소값을 가진 인덱스
def query(node, start, end, l, r):
    # 값이 벗어나면 시스템 최대값으로 저장
    if end < l or start > r:
        return (sys.maxsize,sys.maxsize)
    
    # 범위 내로 들어오면 해당 값 반환
    if l <= start and end <= r:
        return tree[node]

    mid = (start + end) // 2
    left = query(node*2, start, mid, l, r)
    right = query(node*2+1, mid+1, end, l, r)

    return check(left,right)

M = int(input())
for _ in range(M):
    a,b,c = map(int,input().split())
    if a == 1:
        change(1,0,N-1,b-1,c)
    elif a == 2:
        v,idx = query(1,0,N-1,b-1,c-1)
        print(idx+1)