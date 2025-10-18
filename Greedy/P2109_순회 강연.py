import heapq,sys
input = sys.stdin.readline

N = int(input())

# (-p,d) 형태로 튜플을 heap 안에 저장
lecture = []

for _ in range(N):
    p,d = map(int,input().split())
    heapq.heappush(lecture,(-p,d))

max_date = 0
total_fee = [0]*(10001)   # 최종 강연료

while lecture:
    now = heapq.heappop(lecture)
    fee = -now[0]
    deadline = now[1]

    # 1~deadline까지 강의 가능
    for i in range(deadline,0,-1):
        if total_fee[i] == 0:
            total_fee[i] = fee
            break

ans = 0

for i in range(1,10001):
    if total_fee[i] != 0:
        ans += total_fee[i]

print(ans)