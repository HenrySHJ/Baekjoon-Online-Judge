import sys, math
input = sys.stdin.readline

MAX_NUM = 2000

N = int(input())
A = list(map(int,input().split()))

# 최대 숫자까지의 소수 여부
isPrime = [True] * (MAX_NUM + 1)
isPrime[0] = isPrime[1] = False

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(MAX_NUM)) + 1):
    if not isPrime[i]:
        continue

    for j in range(i + i, MAX_NUM + 1, i):
        isPrime[j] = False

# 홀수와 짝수 그룹 분리
left = []
right = []

for x in A:
    # A[0]와 홀짝 여부 같은면 left
    if x % 2 == A[0] % 2:
        left.append(x)
    # A[0]와 홀짝 여부 다르면 right 
    else:
        right.append(x)

# 홀짝 개수가 다른 경우 바로 종료
if len(left) != len(right):
    print(-1)
    sys.exit()

# 이분 매칭 DFS
def DFS(left_idx, cur_right):
    for right_idx in range(len(cur_right)):
        # right_idx의 방문 여부 및 소수 여부 검사
        if visited[right_idx] or not isPrime[left[left_idx] + cur_right[right_idx]]:
            continue
        
        # right_idx 방문 처리
        visited[right_idx] = True

        # right_idx가 매칭이 안됐거나, 매칭되어 있던 left_idx가 다른 데로 갈 수 있는 경우
        if matched[right_idx] == -1 or DFS(matched[right_idx], cur_right):
            matched[right_idx] = left_idx
            return True
    
    return False

ans = []
    
for i in range(len(right)):
    # A[0]와 right[i]의 합이 소수가 아니면 건너뛰기
    if not isPrime[left[0] + right[i]]:
        continue

    # A[0]와 right[i]를 뺀 나머지로 이분 매칭 시도
    temp_right = right[:]
    target_val = temp_right.pop(i)
            
    # matched[j] = right_idx(j)랑 연결되어 있는 left_idx(i)
    matched = [-1] * len(temp_right)
    count = 0
            
    # A[0]를 제외한 1번부터 매칭 시작
    for j in range(1, len(left)):
        visited = [False] * len(temp_right)
        
        if DFS(j, temp_right):
            count += 1
            
    # 모든 쌍이 다 맞춰지는 경우
    if count == len(left) - 1:
        ans.append(target_val)

# 정답 출력
if not ans:
    print(-1)
else:
    ans.sort()
    print(*(ans))