import sys
input = sys.stdin.readline

S = list(input().strip())
streak = [0]*len(S)

idx = 0
i = 0
while i < len(S):
    if S[i] == 'X':
        streak[idx] += 1
        i += 1
    
    elif S[i] == '.':
        i += 1
        idx = i

for i in range(len(S)):
    # 연속 개수가 홀수면 바로 -1, 종료
    if streak[i] % 2 == 1:
        print(-1)
        sys.exit()

    # 연속 정보가 없으면 건너뛰기
    if streak[i] == 0:
        continue
    
    # AAAA 처리
    count1 = 0
    while streak[i] >= 4:
        count1 += 1
        streak[i] -= 4

    for j in range(i,i+count1*4):
        S[j] = 'A'

    count2 = 0
    if streak[i] == 2:
        for j in range(i+count1*4,i+count1*4+2):
            S[j] = 'B'

for i in range(len(S)):
    print(S[i],end='')
    