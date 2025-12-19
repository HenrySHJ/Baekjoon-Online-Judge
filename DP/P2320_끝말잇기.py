import sys
input = sys.stdin.readline

N = int(input())

words = [input().strip() for _ in range(N)]
len_words = [0]*N     # 단어 길이 저장
start_alp = [-1]*N    # 시작 문자 저장
end_alp = [-1]*N     # 종료 문자 저장

for i in range(N):
    len_words[i] = len(words[i])

# 시작 문자에 대해 숫자로 전처리
for i in range(N):
    if words[i][0] == 'A':
        start_alp[i] = 0
    if words[i][0] == 'E':
        start_alp[i] = 1
    if words[i][0] == 'I':
        start_alp[i] = 2
    if words[i][0] == 'O':
        start_alp[i] = 3
    if words[i][0] == 'U':
        start_alp[i] = 4

# 종료 문자에 대해 숫자로 전처리
for i in range(N):
    if words[i][-1] == 'A':
        end_alp[i] = 0
    if words[i][-1] == 'E':
        end_alp[i] = 1
    if words[i][-1] == 'I':
        end_alp[i] = 2
    if words[i][-1] == 'O':
        end_alp[i] = 3
    if words[i][-1] == 'U':
        end_alp[i] = 4

# DP[alp][mask] : 마지막 문자 alp, 단어 사용 mask일때 최대 길이
DP = [[0]*(1<<N) for _ in range(5)]

# DP 초기 상태 설정
for i in range(N):
    DP[end_alp[i]][1<<i] = len_words[i]

# mask 순회하며 답 찾기
for mask in range(1<<N):
    for alp in range(5):
        # 아직 갱신이 되지 않은 상태 건너뛰기
        if DP[alp][mask] == 0:
            continue

        for j in range(N):
            # 이미 한 번 사용한 단어인 경우
            if mask & (1<<j):
                continue

            # 다음 단어의 시작 문자가 연속된 마지막 문자와 같은 경우
            if start_alp[j] == alp:
                nmask = mask | (1<<j)
                DP[end_alp[j]][nmask] = DP[alp][mask] + len_words[j]

ans = 0
for i in range(5):
    for mask in range(1<<N):
        ans = max(ans,DP[i][mask])

print(ans)