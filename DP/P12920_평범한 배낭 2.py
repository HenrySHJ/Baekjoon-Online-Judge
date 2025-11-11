import sys
input = sys.stdin.readline

N,M = map(int,input().split())
things = []
DP = [0]*(M+1)   # 인덱스 : 가방 무게 / 데이터 : 최대 만족도 

for i in range(N):
    V,C,K = map(int,input().split())
    binary = 1
    # K를 2 배수 단위로 끊어서 저장 (이진 분할*)
    while K > 0:
        count = min(binary, K)
        things.append((V*count, C*count))
        K -= count
        binary *= 2

for v, c in things:
    for j in range(M, v-1, -1):
        DP[j] = max(DP[j], DP[j-v] + c)
        
print(DP[M])