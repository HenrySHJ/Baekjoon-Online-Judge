N = int(input())

A = list(map(int,input().split()))
sorted_A = sorted(set(A))

dict_A = {sorted_A[i] : i for i in range(len(sorted_A))}
for i in A:
    print(dict_A[i], end = ' ')