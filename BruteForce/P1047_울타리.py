import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
tree = []   
fence = []

for _ in range(N):
    x,y,f = map(int,input().split())
    tree.append((x,y,f))

tree_x = [t[0] for t in tree]   # x 좌표 리스트
tree_y = [t[1] for t in tree]   # y 좌표 리스트

tree_x = sorted(set(tree_x))
tree_y = sorted(set(tree_y))

ans = INF
# O(N^5) : 울타리 직사각형을 구성하는 x1, x2, y1, y2 선택
for xi1 in range(len(tree_x)):
    for xi2 in range(xi1, len(tree_x)):
        x1 = tree_x[xi1]
        x2 = tree_x[xi2]

        for yi1 in range(len(tree_y)):
            for yi2 in range(yi1, len(tree_y)):
                y1 = tree_y[yi1]
                y2 = tree_y[yi2]

                # 최소 필요 울타리 둘레
                girth = 2*((x2-x1)+(y2-y1))

                outside = []   # 울타리 밖에 있는 나무
                inside = []    # 울타리 안/경계에 있는 나무

                for x, y, v in tree:
                    # 울타리 바깥에 있는 점
                    if not (x1 <= x <= x2 and y1 <= y <= y2):
                        outside.append(v)
                    # 울타리 내부에 있는 점
                    else:
                        inside.append(v)

                # 밖의 나무를 베서 제작 가능한 총 울타리 길이
                min_girth = girth
                outside_sum = sum(outside)
                max_girth = outside_sum

                # 자른 나무 개수 : outside 길이
                cut_count = len(outside)
                
                # 밖만 베서 충분하면 끝
                if max_girth >= min_girth:
                    ans = min(ans, cut_count)
                    continue

                # 부족하면 inside에서 가치 높은 순으로 추가로 베기
                inside.sort(reverse=True)

                for v in inside:
                    max_girth += v
                    cut_count += 1
                    if max_girth >= min_girth:
                        ans = min(ans, cut_count)
                        break

print(ans)