import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int,input().split()))

F = [0]*1000001

for i in range(N):
    F[A[i]] += 1

ans = [-1]*N
stack = []
    
for i in range(N):
    # 스택이 비어있지 않고, A[i]가 스택의 top보다 크면
    while stack and F[A[stack[-1]]] < F[A[i]]:
        # 오등큰수를 찾았으므로 pop 하고 결과 기록
        idx = stack.pop()
        ans[idx] = A[i]
            
    # 현재 인덱스를 스택에 추가
    stack.append(i)

print(*ans)