N = int(input())
check = [True]*(N+1)
check[0] = check[1] = False

# 에라토스테네스의 체
for i in range(2,int(N**0.5)+1):
    if check[i]:
        for j in range(i*i,N+1,i):
            check[j] = False

numlist = []
for i in range(1,N+1):
    if check[i]:
        numlist.append(i)
numlist.insert(0,0)

# 합 배열
sumlist = [0]
for i in range(1,len(numlist)):
    sumlist.append(sumlist[-1]+numlist[i])

ans = 0

# Two_pointer
s = 1
e = 1

while e < len(numlist):
    if sumlist[e] - sumlist[s-1] == N:
        ans += 1
        e += 1
    elif sumlist[e] - sumlist[s-1] > N:
        s += 1
    else:
        e += 1

print(ans)