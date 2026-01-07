import sys
input = sys.stdin.readline

MOD = 1000000

N = int(input())

# 2명 이하일때 특수 처리
if N <= 2:
    print(N)
    sys.exit()

# DP[i][j] : 왼쪽(키 작은) i명, 오른쪽(키 큰) j명 남았을 때의 경우의 수
DP = [[-1]*(N+1) for _ in range(N+1)]

# 기준 숫자보다 작은 개수(l), 큰 개수(r)
def line(l, r):
    # 더 이상 고를 학생이 없을 때
    if l + r == 0:
        return 1
    
    # 이미 갱신됐던 정보면 그대로 이용
    if DP[l][r] != -1:
        return DP[l][r]
        
    res = 0
    # l에 있는 숫자만 고를 후보가 됨 / l = 0이면 자연스럽게 res = 0
    for i in range(1,l+1):
        # i 기준 새로운 작은쪽, 큰쪽 정의하고 작/큰 매개변수 위치 바꿔서 투입
        res = (res + line(r+l-i, i-1)) % MOD
            
    DP[l][r] = res
    return res

ans = 0

# i가 첫번째 학생이 되는 경우를 모두 테스트
for i in range(1,N+1):
    # i보다 작은(left) 개수와 i보다 큰 개수(right)
    left = i-1
    right = N-i

    # 키가 작아지는 경우와 커지는 경우 모두 고려
    ans = (ans + line(left, right)) % MOD
    ans = (ans + line(right, left)) % MOD
        
print(ans % MOD)