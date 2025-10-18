#  n!에 포함된 소수 p의 개수
def count_p(n, p):
    cnt = 0
    while n:
        n //= p
        cnt += n
    return cnt

# n의 소인수분해 결과를 딕셔너리 {p: a}
def prime(n):
    factors = {}
    d = 2
    # d <= sqrt(N)까지 수행
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

S, F, M = map(int, input().split())

for i in range(M,0,-1):
    factors = prime(i)
    possible = True

    for p, a in factors.items():
        # (S+F)!/(S!*F!)에서 p 개수는 무조건 분자가 많아야 함
        cnt = count_p(S + F, p) - count_p(S, p) - count_p(F, p)
        
        # p 개수가 분모가 더 많을 시 적절하지 않은 숫자
        if cnt < a:
            possible = False
            break

    if possible:
        print(i)
        break
    if i == 1:
        print(-1)