import sys
input = sys.stdin.readline

N,K,D = map(int,input().split())

student = []
for _ in range(N):
    M,d = map(int,input().split())
    A = list(map(int,input().split()))
    student.append((d,A))
student.sort(key=lambda x:x[0])

# Two Pointer
l = 0
r = 0

ans = 0
alg_count = [0]*(K+1)
count_u = 0

# r 포인터를 1씩 우로 이동시키면서
for r in range(N):
    # r 포인터 +1에 따른 합집합 정리
    for alg in student[r][1]:
        if alg_count[alg] == 0:
            count_u += 1
        alg_count[alg] += 1

    # D 조건에 따른 l 포인터 이동
    while student[r][0] - student[l][0] > D:
        # l 포인터 이동에 따른 합집합 정리
        for alg in student[l][1]:
            alg_count[alg] -= 1
            if alg_count[alg] == 0:
                count_u -= 1 
        l += 1

    count_s = r - l + 1
    count_i = 0

    # 교집합 개수 세기
    for k in range(1,K+1):
        if alg_count[k] == count_s:
            count_i += 1
                
    ans = max(ans,(count_u-count_i)*count_s)
            
print(ans)