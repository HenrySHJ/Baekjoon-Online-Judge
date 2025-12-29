import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    debt = [list(map(int,input().split())) for _ in range(N)]
    sum_debt = [sum(debt[i]) for i in range(N)]

    # DP[mask] : mask(1이면 파산 상태로 표기)일때 존재하는 케이스면 True
    DP = [False]*(1<<N)
    DP[0] = True

    for mask in range(1<<N):
        # 존재하지 않는 케이스 건너뛰기
        if not DP[mask]:
            continue

        for i in range(N):
            # mask에 i가 이미 포함된 경우 건너뛰기
            if mask & (1<<i):
                continue

            cur_debt = sum_debt[i]
            for j in range(N):
                # mask에 j가 없으면 부채 유효
                if not mask & (1<<j):
                    continue

                # 부채 계산
                cur_debt -= debt[i][j]

            # 새로 계산된 부채가 양수라면 파산 가능
            if cur_debt > 0:
                nmask = mask | (1<<i)
                DP[nmask] = True

    # 정답 출력
    full_bit = (1<<N)-1

    ans = []
    for i in range(N):
        # 왕국이 혼자 사는 경우 확인하기
        if DP[full_bit ^ (1<<i)]:
            ans.append(i+1)

    if ans:
        print(*ans)
    else:
        print(0)