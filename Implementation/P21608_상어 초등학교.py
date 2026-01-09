import sys
input = sys.stdin.readline

N = int(input())
student_info = {}
order = []

for _ in range(N**2):
    line = list(map(int, input().split()))
    student_info[line[0]] = set(line[1:])
    order.append(line[0])

desk = [[0]*N for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 학생 순서대로 처리하기
for s_num in order:
    cand = []

    for i in range(N):
        for j in range(N):
            # 비어있는 책상 상태에서 상/하/좌/우 뻗기
            if desk[i][j] == 0:
                like_cnt = 0
                empty_cnt = 0

                # 주변에 좋아하는 학생 / 비어있는 책상 개수 세기
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]

                    # 좌표 유효성 검사
                    if 0 <= ni < N and 0 <= nj < N:
                        # 좋아하는 학생 세기
                        if desk[ni][nj] in student_info[s_num]:
                            like_cnt += 1

                        # 비어있는 책상 세기
                        elif desk[ni][nj] == 0:
                            empty_cnt += 1

                cand.append((-like_cnt,-empty_cnt,i,j))
    
    # 1순위: like_cnt 내림차순, 2순위: empty_cnt 내림차순, 3순위: 행 오름차순, 4순위: 열 오름차순
    cand.sort()
    x,y = cand[0][2],cand[0][3]

    # 최종 배치
    desk[x][y] = s_num

# 만족도 계산
ans = 0
score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}

for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]

            # 좌표 유효성 검사
            if 0 <= ni < N and 0 <= nj < N:
                # 만족도 연산
                if desk[ni][nj] in student_info[desk[i][j]]:
                    cnt += 1
        ans += score[cnt]

print(ans)