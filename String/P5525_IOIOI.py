import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
S = input().strip()

ans = 0
consecution = 0
i = 1

while i < M - 1:
    # 'OI' 패턴 이어지는 경우
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        consecution += 1

        # Pn 보다 커지면 정답 추가
        if consecution >= N:
            ans += 1

        i += 2
    # 'OI' 패턴 끊기는 경우
    else:
        consecution = 0
        i += 1

print(ans)
