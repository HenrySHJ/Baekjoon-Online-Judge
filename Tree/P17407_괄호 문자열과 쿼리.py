import sys
input = sys.stdin.readline

S = list(input())
S.pop()
length = len(S)

tree_check = [0]*(4*length)  # 음수가 존재하면 올바르지 않은 문자열
lazy = [0]*(4*length)

# tree_check 함수 채우기
def build(node,start,end):
    # 리프 노드에 누적 합 저장
    if start == end:
        tree_check[node] = sum_list[start]
        return
    
    mid = (start + end) // 2

    build(node*2,start,mid)
    build(node*2+1,mid+1,end)

    # tree_check는 리프의 최솟값을 받아서 올바른 문자열 추가 판별
    tree_check[node] = min(tree_check[node*2], tree_check[node*2+1])

# lazy 적용 함수
def propagate(node,start,end):
    if lazy[node] != 0:
        tree_check[node] += lazy[node]
        
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]

        lazy[node] = 0

# sum_list의 변화 인덱스 범위 : q-1 ~ N-1  -> lazy 처리
def change(node,start,end,l,r,n):
    propagate(node,start,end)
    # 범위를 벗어난 경우의 처리
    if start > r or end < l:
        return
    
    if start >= l and end <= r:
        lazy[node] += n
        propagate(node,start,end)
        return

    mid = (start + end) // 2

    change(node*2,start,mid,l,r,n)
    change(node*2+1,mid+1,end,l,r,n)

    tree_check[node] = min(tree_check[node*2], tree_check[node*2 + 1])

M = int(input())
ans = 0

# sum_list : S의 누적 합
sum_list = [0]*length

if S[0] =='(':
    sum_list[0] = 1
elif S[0] ==')':
    sum_list[0] = -1

for i in range(1,length):
    if S[i] =='(':
        sum_list[i] = sum_list[i-1] + 1
    elif S[i] ==')':
        sum_list[i] = sum_list[i-1] - 1

build(1,0,length-1)

# count : '(' 개수 - ')' 개수
count = sum_list[-1]

for _ in range(M):
    q = int(input())
    
    if S[q-1] == '(':
        count -= 2
        change(1,0,length-1,q-1,length-1,-2)
        S[q-1] = ')'

    elif S[q-1] == ')':
        count += 2
        change(1,0,length-1,q-1,length-1,2)
        S[q-1] = '('

    if count == 0 and tree_check[1] >= 0:
        ans += 1

print(ans)