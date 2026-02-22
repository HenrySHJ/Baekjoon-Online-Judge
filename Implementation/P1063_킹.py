import sys
input = sys.stdin.readline

king, stone, N = input().split()

K = [int(king[1]) - 1, ord(king[0]) - ord('A')]
S = [int(stone[1]) - 1, ord(stone[0]) - ord('A')]
N = int(N)

for _ in range(N):
    move = input().strip()

    if move == 'R':
        if 0 <= K[1] + 1 < 8:
            if K[1] + 1 == S[1] and K[0] == S[0]:
                if 0 <= S[1] + 1 < 8:
                    K[1] += 1
                    S[1] += 1
            else:
                K[1] += 1

    elif move == 'L':
        if 0 <= K[1] - 1 < 8:
            if K[1] - 1 == S[1] and K[0] == S[0]:
                if 0 <= S[1] - 1 < 8:
                    K[1] -= 1
                    S[1] -= 1
            else:
                K[1] -= 1

    elif move == 'T':
        if 0 <= K[0] + 1 < 8:
            if K[1] == S[1] and K[0] + 1 == S[0]:
                if 0 <= S[0] + 1 < 8:
                    K[0] += 1
                    S[0] += 1
            else:
                K[0] += 1

    elif move == 'B':
        if 0 <= K[0] - 1 < 8:
            if K[1] == S[1] and K[0] - 1 == S[0]:
                if 0 <= S[0] - 1 < 8:
                    K[0] -= 1
                    S[0] -= 1
            else:
                K[0] -= 1

    elif move == 'RT':
        if 0 <= K[1] + 1 < 8 and 0 <= K[0] + 1 < 8:
            if K[1] + 1 == S[1] and K[0] + 1 == S[0]:
                if 0 <= S[1] + 1 < 8 and 0 <= S[0] + 1 < 8:
                    K[1] += 1
                    K[0] += 1
                    S[1] += 1
                    S[0] += 1
            else:
                K[1] += 1
                K[0] += 1

    elif move == 'LT':
        if 0 <= K[1] - 1 < 8 and 0 <= K[0] + 1 < 8:
            if K[1] - 1 == S[1] and K[0] + 1 == S[0]:
                if 0 <= S[1] - 1 < 8 and 0 <= S[0] + 1 < 8:
                    K[1] -= 1
                    K[0] += 1
                    S[1] -= 1
                    S[0] += 1
            else:
                K[1] -= 1
                K[0] += 1

    elif move == 'RB':
        if 0 <= K[1] + 1 < 8 and 0 <= K[0] - 1 < 8:
            if K[1] + 1 == S[1] and K[0] - 1 == S[0]:
                if 0 <= S[1] + 1 < 8 and 0 <= S[0] - 1 < 8:
                    K[1] += 1
                    K[0] -= 1
                    S[1] += 1
                    S[0] -= 1
            else:
                K[1] += 1
                K[0] -= 1

    elif move == 'LB':
        if 0 <= K[1] - 1 < 8 and 0 <= K[0] - 1 < 8:
            if K[1] - 1 == S[1] and K[0] - 1 == S[0]:
                if 0 <= S[1] - 1 < 8 and 0 <= S[0] - 1 < 8:
                    K[1] -= 1
                    K[0] -= 1
                    S[1] -= 1
                    S[0] -= 1
            else:
                K[1] -= 1
                K[0] -= 1

print(chr(K[1] + ord("A")) + str(K[0] + 1))
print(chr(S[1] + ord("A")) + str(S[0] + 1))