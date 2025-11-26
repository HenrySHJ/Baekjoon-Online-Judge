import sys
input = sys.stdin.readline

N = int(input())

# 숫자를 사전상 순서로 처리하기 위해 str형태로 입력받기
A = list(input().split())

# 문자열 a+b,b+a 비교
for i in range(N):
    for j in range(i+1,N):
        if A[i] + A[j] < A[j] + A[i]:
            A[i],A[j] = A[j],A[i]

ans = ''
for i in range(N):
    ans += A[i]

print(int(ans))

# A.sort(key=lambda x : x**10,reversed=True)
# 시간 복잡도를 더 감소 시키고 풀 수 있음