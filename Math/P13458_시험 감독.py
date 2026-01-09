import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())

ans = 0
for i in range(N):
    # 메인 시험관
    A[i] -= B
    ans += 1

    # 남은 응시자가 있을 때만 부감독관 배치
    if A[i] > 0:
        if A[i] % C == 0:
            ans += A[i] // C
        else:
            ans += (A[i] // C) + 1

print(ans)