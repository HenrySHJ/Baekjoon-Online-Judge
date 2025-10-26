import sys
input = sys.stdin.readline

N,M = map(int,input().split())

k = 0
while 2**k < N:
    k += 1

tree_min = [0]*(2**(k+1))
tree_max = [0]*(2**(k+1))
leafstart = 2**k

for i in range(N):
    n = int(input())
    tree_min[leafstart + i] = n
    tree_max[leafstart + i] = n

# 상위 노드 채우기
for i in range(leafstart - 1,0,-1):
    tree_min[i] = min(tree_min[i*2],tree_min[i*2 + 1])
    tree_max[i] = max(tree_max[i*2],tree_max[i*2 + 1])

# 최솟값 찾기
def min_query(node,start,end,l,r):
    if r < start or end < l:
        return sys.maxsize
    
    if start >= l and end <= r:
        return tree_min[node]
    
    mid = (start + end) // 2

    return min(min_query(node*2,start,mid,l,r),min_query(node*2+1,mid+1,end,l,r))

# 최댓값 찾기
def max_query(node,start,end,l,r):
    if r < start or end < l:
        return -sys.maxsize
    
    if start >= l and end <= r:
        return tree_max[node]
    
    mid = (start + end) // 2

    return max(max_query(node*2,start,mid,l,r), max_query(node*2+1,mid+1,end,l,r))

for _ in range(M):
    a,b = map(int,input().split())
    print(min_query(1,0,2**k-1,a-1,b-1),max_query(1,0,2**k-1,a-1,b-1))