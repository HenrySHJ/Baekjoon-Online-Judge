import sys
input = sys.stdin.readline

N = int(input())
dice = list(map(int,input().split()))

a = min(dice[0],dice[5])
b = min(dice[1],dice[4])
c = min(dice[2],dice[3])
num_list = [a,b,c]
num_list.sort()

ans = 0
# 주사위가 하나면 최댓값만 안 보이게
if N == 1:
    print(sum(dice)-max(dice))

if N >= 2:
    # 옆 면의 외각 제외 처리
    ans += 4*num_list[0]*(N-1)*(N-1)
    ans += 4*num_list[1]*(N-1)

    ans += num_list[0]*N*N
    ans += num_list[1]*(N-1)*4
    ans += num_list[2]*4

    print(ans)