import sys
input = sys.stdin.readline

N, S = map(int, input().split())

# 정점이 2개 이하면 항상 0
if N <= 2:
    print(0)
    sys.exit()

# DP[i][j] : 정점 i개, 단순 경로 j개일때 가능여부
DP = [[False]*(S+1) for _ in range(N+1)]
    
# DP 초기화
DP[2][0] = True

# i(정점 개수)로 i+1 완성
for i in range(2,N):
    # j(단순 경로)는 i-2부터 가능
    for j in range(i-2,S+1):
        # 초기화가 안된 경우 건너뛰기
        if not DP[i][j]:
            continue
            
        # 하나의 리프 노드에 k개의 자식노드를 붙이기
        for k in range(1,N-i+1):
            # 리프노드로 연결되는 간선 + k개의 간선 (k+1)C2
            add_paths = k*(k+1)//2
            if j + add_paths <= S:
                DP[i+k][j+add_paths] = True

if DP[N][S]:
    print(1)
else:
    print(0)