A, B, C = map(int, input().split())

def solve(a, b, c):
    if b == 1:
        return a % c
    
    # 지수를 절반으로 나누어 재귀 호출
    temp = solve(a, b // 2, c)
    
    # 짝수면 두 개 그대로 합치기
    if b % 2 == 0:
        return (temp * temp) % c
    # 홀수면 두 개에 a 하나 추가
    else:
        return (temp * temp * a) % c

print(solve(A, B, C))