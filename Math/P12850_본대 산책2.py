import sys
input = sys.stdin.readline

MOD = 1000000007

# 인접 행렬로 이동 경로
buildings = [
    [0, 1, 1, 0, 0, 0, 0, 0], # 정보과학관
    [1, 0, 1, 1, 0, 0, 0, 0], # 전산관
    [1, 1, 0, 1, 1, 0, 0, 0], # 미래관
    [0, 1, 1, 0, 1, 1, 0, 0], # 신양관
    [0, 0, 1, 1, 0, 1, 0, 1], # 한경직기념관
    [0, 0, 0, 1, 1, 0, 1, 0], # 진리관
    [0, 0, 0, 0, 0, 1, 0, 1], # 형남공학관
    [0, 0, 0, 0, 1, 0, 1, 0]  # 학생회관
]

# 두 개의 행렬 곱셈 연산
def multiply(A, B):
    C = [[0] * 8 for _ in range(8)]

    # (i에서 k) * (k에서 j)로 i에서 j로 가는 경우의 수를 곱하기
    for i in range(8):
        for j in range(8):
            for k in range(8):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD

    # 행렬 결과 반환
    return C

# 분할 정복 거듭제곱
def power(building, d):
    # d가 1이면 행렬 그대로 반환
    if d == 1:
        return building
    
    half = power(building, d // 2)

    # d를 절반으로 나누어가며 연산 시간 단축
    if d % 2 == 0:
        return multiply(half, half)
    else:
        return multiply(multiply(half, half), building)

D = int(input())
result = power(buildings, D)

print(result[0][0])