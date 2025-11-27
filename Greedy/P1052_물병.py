import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ans = 0

while bin(N).count('1') > K:
    # 물병 구매량 : N의 가장 오른쪽 비트
    add = N & -N
    ans += add
    N += add

print(ans)