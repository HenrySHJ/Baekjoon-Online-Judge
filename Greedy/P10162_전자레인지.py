import sys
input = sys.stdin.readline
A = 300
B = 60
C = 10

T = int(input())
a = b = c = 0
while T >= 300:
    T -= A
    a += 1

while T >= 60:
    T -= B
    b += 1

while T >= 10:
    T -= C
    c += 1

if T == 0:
    print(a,b,c)
else:
    print(-1)