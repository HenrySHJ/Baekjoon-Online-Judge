import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    N,M = map(int,input().split())

    desk = [0]*N

    # 비트 연산을 위해 'x'자리를 1, 앉을 수 있는 자리를 0으로 전처리
    A = [list(input().strip()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if A[i][j] == 'x':
                desk[i] |= (1<<j)

    # DP[i][mask] : i번째 열의 현재 mask 상태에서 최대의 인원이 앉을 때
    DP = [[-1]*(1<<M) for _ in range(N)]

    # 가능한 mask 상태를 미리 종합해 놓기
    candidate_mask = []
    for mask in range(1<<M):
        if not (mask & (mask<<1)):
            candidate_mask.append(mask)

    # 1행 따로 처리
    for mask in candidate_mask:
        # 앉을 수 없는 자리에 1 있는 경우 건너뛰기
        if mask & desk[0]:
            continue
        DP[0][mask] = bin(mask).count('1')

    # 2행 ~ N행
    for i in range(1,N):
        for mask in candidate_mask:
            # 앉을 수 없는 자리에 1 있는 경우 건너뛰기
            if mask & desk[i]:
                continue
            
            # i-1행 검사를 통해 갱신 가능 여부 확인
            count = bin(mask).count('1')
            for prev_mask in candidate_mask:
                # 갱신된 적이 없던 경우 건너뛰기
                if DP[i-1][prev_mask] == -1:
                    continue

                # 대각선 컨닝 방지
                if prev_mask & (mask<<1) or prev_mask & (mask>>1):
                    continue
                
                # DP 갱신
                DP[i][mask] = max(DP[i][mask],DP[i-1][prev_mask] + count)
    
    print(max(DP[N-1]))