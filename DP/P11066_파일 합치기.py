import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    file = list(map(int,input().split()))
    file.insert(0,0)

    # 누적합
    S = [0] * (K+1)
    for i in range(1, K+1):
        S[i] = S[i-1] + file[i]

    # DP[i][j] : i~j까지를 합칠때의 최소
    DP = [[0]*(K+1) for _ in range(K+1)]
    # i~j를 합칠때의 분단점 인덱스
    idx = [[0]*(K+1) for _ in range(K+1)]
    
    # 구간의 길이를 늘려가면서 메모제이션
    for length in range(2,K+1):
        for l in range(1, K-length+2):
            r = l + length - 1
            DP[l][r] = sys.maxsize

            s = idx[l][r-1]
            e = idx[l+1][r]
            # 기존 분단점이 존재하지 않으면 양 끝으로
            if s == 0: s = l
            if e == 0: e = r-1

            for k in range(s, e+1):
                # l~r의 비용 : l~k + k~r의 비용 + 구간의 전체 합
                cost = DP[l][k] + DP[k+1][r] + (S[r] - S[l-1])
                # 기존 비용보다 작으면 갱신
                if DP[l][r] > cost:
                    DP[l][r] = cost
                    idx[l][r] = k

    print(DP[1][K])