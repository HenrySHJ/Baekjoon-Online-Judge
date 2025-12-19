import sys
input = sys.stdin.readline

K = int(input())
inorder = list(map(int,input().split()))
tree = [0]*(2**K)

idx = 0
def build(node):
    global idx
    if node*2 < 2**K:
        build(node*2)
    tree[node] = inorder[idx]
    idx += 1
    if node*2 + 1< 2**K:
        build(node*2 + 1)

build(1)
k = 0
while k != K:
    for i in range(2**k,2**(k+1)):
        print(tree[i],end=' ')
    k += 1
    print()