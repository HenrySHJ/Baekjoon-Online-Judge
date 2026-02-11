import sys
input = sys.stdin.readline

MOD = 1000

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 행렬 곱 연산
def multiply_matrix(matrix1, matrix2):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] = (result[i][j] + matrix1[i][k] * matrix2[k][j]) % MOD

    return result

# 분할 정복 거듭제곱
def divide_conquer(matrix, count):
    if count == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A

    # 절반으로 분할하기
    half = divide_conquer(matrix, count // 2)

    if count % 2 == 0:
        return multiply_matrix(half, half)
    else:
        return multiply_matrix(multiply_matrix(half, half), matrix)

ans_matrix = divide_conquer(A, B)

for i in range(N):
    print(*ans_matrix[i])