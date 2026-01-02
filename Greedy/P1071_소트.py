import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
    
count = Counter(A)
num_list = sorted(count.keys())
    
ans = []
    
i = 0
# i번째 숫자인 cur을 전부 털면서 규칙에 따라 다른 숫자를 털어야함
while i < len(num_list):
    cur = num_list[i]
        
    # 이미 다 쓴 숫자는 넘어감
    if count[cur] == 0:
        i += 1
        continue
            
    # 다음 숫자가 유효 숫자인지 확인
    if i+1 < len(num_list):
        nxt = num_list[i+1]
            
        # nxt : cur이랑 연속되는 숫자가 있는 경우
        if cur + 1 == nxt and count[nxt] > 0:
            # nnxt(다다음 숫자) 확인
            if i + 2 < len(num_list):
                # nnxt(다다음 숫자)가 있으면 cur 모두 털기
                ans.extend([cur]*count[cur])
                count[cur] = 0

                # 이후에 nnxt 한개만 이어붙이기
                nnxt = num_list[i+2]
                ans.append(nnxt)
                count[nnxt] -= 1

            # nnxt가 존재하지 않는 경우
            else:
                # cur+1, cur 순으로 처리하기
                ans.extend([nxt]*count[nxt])
                count[nxt] = 0

                ans.extend([cur]*count[cur])
                count[cur] = 0
                i += 2
        # cur이랑 연속되는 숫자가 없는 경우 : cur 모두 털기
        else:
            ans.extend([cur] * count[cur])
            count[cur] = 0
            i += 1

    # nxt(다음 숫자)가 존재하지 않으면 남은 cur 털기
    else:   
        ans.extend([cur]*count[cur])
        count[cur] = 0
        i += 1

print(*ans)