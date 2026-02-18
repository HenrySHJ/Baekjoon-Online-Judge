import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

ans = []
while True:
    # 두 배열에 공통으로 존재하는 수들 찾기
    common = set(A) & set(B)
    
    # 공통적인 수 존재하지 않으면 종료
    if not common:
        break
    
    # 공통 원소 중 최댓값 넣기
    max_val = max(common)
    ans.append(max_val)

    # 해당 값이 처음 나타나는 위치 찾기 
    idx_A = -1
    idx_B = -1
    for i in range(N):
        if A[i] == max_val:
            idx_A = i
            break

    for j in range(M):
        if B[j] == max_val:
            idx_B = j
            break
    
    # 해당 인덱스 이후로만 배열 저장
    A = A[idx_A + 1:]
    B = B[idx_B + 1:]

print(len(ans))

if ans:
    print(*ans)