import sys
input = sys.stdin.readline

while True:
    A,B,C = map(int,input().split())

    if A == 0 and B == 0 and C == 0:
        break

    lst = []
    lst.append(A)
    lst.append(B)
    lst.append(C)
    lst.sort()

    if lst[0] + lst[1] <= lst[2]:
        print("Invalid")

    elif A == B and B == C:
        print("Equilateral")

    elif A == B or B == C or C == A:
        print("Isosceles")

    else:
        print("Scalene")