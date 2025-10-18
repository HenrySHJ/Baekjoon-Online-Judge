def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

N, A = map(int, input().split())

# 덧셈 역원
add_inverse = (N - A) % N

# 곱셈 역원
g, x, y = extended_gcd(A, N)

if g != 1:
    print(add_inverse, -1)
else:
    mul_inverse = x % N
    print(add_inverse, mul_inverse)