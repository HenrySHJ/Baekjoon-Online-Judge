import sys
input = sys.stdin.readline

N,K = map(int,input().split())

# 할 일의 순서를 저장한 리스트
task = list(map(int,input().split()))

# 현재 멀티탭
tab = []
ans = 0

for i in range(K):
    cur = task[i]

    # 이미 꽂혀있는 경우 패스
    if cur in tab:
        continue

    # 멀티탭 공간 있으면 꽂기
    if len(tab) < N:
        tab.append(cur)
        continue

    # 교체 대상 찾기
    far_idx = -1
    target = -1

    for t in tab:
        # 앞으로 더 이상 쓸 일이 없는 경우
        if t not in task[i+1:]:
            target = t
            break
        # 다시 쓰일 경우 중 제일 나중에 쓰는 경우 제거
        else:
            # 탭에 존재하는 재등장 인덱스 중 제일 큰 값 찾기
            next = task[i+1:].index(t)
            if next > far_idx:
                far_idx = next
                target = t

    # 멀티탭 구멍 교체
    tab[tab.index(target)] = cur
    ans += 1

print(ans)