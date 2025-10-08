def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

T = int(input())

for _ in range(T):
    K,C = map(int,input().split())

    # 특수 케이스 처리
    if C == 1:
        if K+1 > 1000000000:
            print("IMPOSSIBLE")
        else:
            print(K+1)
        continue
    elif K == 1:
        print(1)
        continue
    
    # Cy(구매할 사탕 개수)-Kx(뿌려질 사탕 개수) = 1 / x: 인원 수, y: 사탕 봉지 수
    g, y, x = extended_gcd(C,K)

    # y를 양수로
    y %= K

    # 해가 존재하지 않음
    if g != 1:
        print("IMPOSSIBLE")
        continue

    # 10**9면 불가능
    if y > 1000000000:
        print("IMPOSSIBLE")
    else:
        print(y)