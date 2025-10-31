N = int(input())

score1 = 100
score2 = 100

for _ in range(N):
    a,b = map(int,input().split())
    if a > b:
        score2 -= a
    elif a < b:
        score1 -= b

print(score1)
print(score2)