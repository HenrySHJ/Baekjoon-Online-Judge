import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    password = input().strip()

    # 커서 기준 좌우 나누기
    left = []
    right = []

    for p in password:
        if p == '<':
            if left:
                right.append(left.pop())

        elif p == '>':
            if right:
                left.append(right.pop())

        elif p == '-':
            if left:
                left.pop()

        else:
            left.append(p)

    for i in range(len(left)):
        print(left[i], end = "")
    
    for i in range(len(right) - 1, -1, -1):
        print(right[i], end = "")
    print()