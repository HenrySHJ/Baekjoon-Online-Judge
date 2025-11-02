N = int(input())
M = (2*N - 1)

for i in range(1,N+1):
    K = 2*i - 1
    print(" "*((M-K)//2)+"*"*K)


for i in range(N-1,0,-1):
    K = 2*i - 1
    print(" "*((M-K)//2)+"*"*K)