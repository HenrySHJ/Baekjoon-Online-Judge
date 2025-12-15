import sys
input = sys.stdin.readline

INF = 10**17
N = int(input())
street = list(input().strip())

# DP[i] : 0~i 까지 도달하기 위한 최소 에너지
DP = [INF]*N
DP[0] = 0

for i in range(N):
    for j in range(i+1,N):
        if street[i] == 'B' and street[j] == 'O':
            DP[j] = min(DP[j],DP[i]+(j-i)**2)
            
        elif street[i] == 'O' and street[j] == 'J':
            DP[j] = min(DP[j],DP[i]+(j-i)**2)

        elif street[i] == 'J' and street[j] == 'B':
            DP[j] = min(DP[j],DP[i]+(j-i)**2)

print(DP[N-1] if DP[N-1] != INF else -1)