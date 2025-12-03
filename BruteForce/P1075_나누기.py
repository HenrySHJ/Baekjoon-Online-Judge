N = int(input())
F = int(input())

N = (N//100)*100

while N % F != 0:
    N += 1

ans = str(N - (N//100)*100)

if len(ans) == 1:
    ans = '0'+ans
print(ans)