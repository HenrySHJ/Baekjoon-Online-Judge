import sys
input = sys.stdin.readline

N = int(input())
Crane = list(map(int,input().split()))
Crane.sort(reverse=True)

M = int(input())
box = list(map(int,input().split()))
box.sort(reverse=True)

# 제일 무거운 박스 > 제한무게
if Crane[0] < box[0]:
    print(-1)
    sys.exit()

ans = 0
while box:
    ans += 1
    for c in Crane:
        # 들 수 있는 박스를 찾으면 다음 크레인으로
        for i in range(len(box)):
            if c >= box[i]:
                box.pop(i)
                break

print(ans)