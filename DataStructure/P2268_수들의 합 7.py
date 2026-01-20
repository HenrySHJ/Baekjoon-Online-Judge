import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 펜윅 트리
tree = [0]*(N+1)
arr = [0]*(N+1)  # 원본 배열

# 값 바꾸기
def update(i, diff):
    while i <= N:
        tree[i] += diff

        # i & -i로 i의 가장 오른쪽에 있는 1비트를 찾습니다.
        i += (i & -i)

# 1부터 i까지의 부분합
def query(i):
    s = 0
    while i > 0:
        s += tree[i]

        # i의 가장 오른쪽 1비트를 0으로
        i -= (i & -i)
    return s

for _ in range(M):
    q, a, b = map(int, input().split())
    
    if q == 0:
        if a > b:
            a, b = b, a
        # (1 ~ b) 까지의 합 - (1 ~ a-1) 까지의 합
        print(query(b) - query(a - 1))
        
    else:
        # 바꿀값 - 현재 값으로 갱신
        diff = b - arr[a]
        arr[a] = b 
        update(a, diff)