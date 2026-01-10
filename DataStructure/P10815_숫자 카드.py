import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
A.sort()

M = int(input())
B = list(map(int,input().split()))

def binary_search(start,end,target):
    if start == end and A[start] != target:
        return 0
    
    mid = (start+end)//2

    if A[mid] == target:
        return 1
    
    if A[mid] > target:
        return binary_search(start,mid,target)
    elif A[mid] < target:
        return binary_search(mid+1,end,target)

ans = [0]*M
for i in range(M):
    in_A = binary_search(0,N-1,B[i])

    if in_A == 1:
        ans[i] = 1

print(*ans)