import sys
input = sys.stdin.readline

N,M = map(int,input().split())

switch = [0]*(4*N)   # 초기 스위치는 모두 꺼져있는 상태
lazy = [0]*(4*N)

def update(node,start,end,l,r):
    mid = (start + end) // 2

    if lazy[node] != 0:
        # 새로운 값 = 현재 측정 범위 - 현재 값
        switch[node] = lazy[node] - switch[node]
        # 하위 노드가 존재하면 lazy값
        if start != end:
            lazy[node*2] = mid - start + 1 - lazy[node*2]
            lazy[node*2 + 1] = end - mid - lazy[node*2 + 1]
        # 적용 후 0으로
        lazy[node] = 0

    # 범위 벗어날 경우 처리
    if end < l or r < start:
        return
    
    # 범위 내로 들어올 경우
    if start >= l and end <= r:
        # 새로운 값 = 현재 측정 범위 - 현재 값
        switch[node] = (end - start + 1) - switch[node]
        # 하위 노드가 존재하면 lazy값 주기
        if start != end:
            lazy[node*2] = mid - start + 1 - lazy[node*2]
            lazy[node*2 + 1] = end - mid - lazy[node*2 + 1]
        return

    update(node*2,start,mid,l,r)
    update(node*2 + 1, mid+1,end,l,r)
    
    switch[node] = switch[node*2] + switch[node*2 + 1]
    
def query(node,start,end,l,r):
    mid = (start + end) // 2

    if lazy[node] != 0:
        # 새로운 값 = 현재 측정 범위 - 현재 값
        switch[node] = lazy[node] - switch[node]
        # 하위 노드가 존재하면 lazy값 주기
        if start != end:
            lazy[node*2] = mid - start + 1 - lazy[node*2]
            lazy[node*2 + 1] = end - mid - lazy[node*2 + 1]
        # 적용 후 0으로
        lazy[node] = 0

    # 범위를 벗어나면
    if start > r or end < l:
        return 0
    
    # 범위 내로 들어오면 답에 추가
    if start >= l and end <= r:
        return switch[node]

    return query(node*2,start,mid,l,r) + query(node*2+1,mid+1,end,l,r)

for _ in range(M):
    temp = list(map(int,input().split()))
    O,S,T = temp[0],temp[1],temp[2]
    if O == 0:
        update(1,0,N-1,S-1,T-1)

    elif O == 1:
        print(query(1,0,N-1,S-1,T-1))