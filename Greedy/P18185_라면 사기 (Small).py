import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split())) + [0,0]   # 연산 편의 위해 추가

ans = 0
# i+1, i+2 비교에 따른 묶음 소비 순서
for i in range(N):
    # 1) A[i+1]을 가능한 A[i+2]에 맞춰줄 때까지 5원 묶음으로 소비
    # 2) A[i]가 남아있다면 7원 묶음 소비
    if A[i+1] > A[i+2]:
        # 5원 묶음 소비 
        # A[i]가 0이 될때까지 / A[i+1]이 A[i+2]랑 같아질 때까지
        m = min(A[i], A[i+1]-A[i+2])
        ans += 5*m
        A[i] -= m
        A[i+1] -= m

        # 7원 묶음 소비
        # A[i],A[i+1],A[i+2]의 최솟값만큼 소비
        m = min(A[i], A[i+1], A[i+2])
        ans += 7 * m
        A[i] -= m
        A[i+1] -= m
        A[i+2] -= m

    # 1) A[i], A[i+1], A[i+2] 중 하나가 0이 될 때까지 7원 묶음 소비
    # 2) A[i]가 남아있다면 5원 묶음 소비
    else:
        # 7원 묶음 소비
        # A[i],A[i+1],A[i+2]의 최솟값만큼 소비
        m = min(A[i], A[i+1], A[i+2])
        ans += 7*m
        A[i] -= m
        A[i+1] -= m
        A[i+2] -= m

        # 5원 묶음 소비 
        # A[i] 또는 A[i+1]가 0이 될 때까지
        m = min(A[i], A[i+1])
        ans += 5*m
        A[i] -= m
        A[i+1] -= m

    # 3원 묶음 소비 : 남은 숫자 처리
    ans += 3*A[i]

print(ans)