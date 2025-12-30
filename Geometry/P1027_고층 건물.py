import sys
input = sys.stdin.readline

N = int(input())
building = list(map(int,input().split()))
vision = [0]*N

for i in range(N):
    min_incline = sys.maxsize
    for j in range(i-1,-1,-1):
        incline = (building[i]-building[j]) / (i-j)
        
        if incline < min_incline:
            min_incline = incline
            vision[i] += 1

    max_incline = -sys.maxsize
    for j in range(i+1,N):
        incline = (building[j]-building[i])/(j-i)
        
        if incline > max_incline:
            max_incline = incline
            vision[i] += 1

print(max(vision))