N = int(input())
A = list(map(int,input().split()))
num_list = [0]*(1001)
for i in range(2,1001):
    num_list[i] = i

for i in range(2,int(1000**0.5)+1):
    if num_list[i] == 0:
        continue
    else:
        for j in range(i*i,1001,i):
            num_list[j] = 0

ans = 0
for i in range(len(A)):
    if num_list[A[i]] != 0:
        ans += 1

print(ans)