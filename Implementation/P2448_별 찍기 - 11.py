N = int(input())

# 별 찍기 함수
def draw_star(n):
    # 기본 삼각형
    if n == 3:
        return ["  *  ", " * * ", "*****"]

    # 재귀적으로 이전 단계의 별들을 가져옴
    stars = draw_star(n // 2)
    result = []

    # 위쪽 부분: 공백 + 별 + 공백
    for s in stars:
        result.append(" " * (n // 2) + s + " " * (n // 2))

    # 아래쪽 부분: 별 + 공백 + 별
    for s in stars:
        result.append(s + " " + s)

    return result             

draw_star(N)
print('\n'.join(draw_star(N)))