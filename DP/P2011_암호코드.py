import sys
input = sys.stdin.readline

MOD = 1000000

code = [0]+list(input().strip())
if code[1] == '0':
    print(0)
    sys.exit()

DP = [0]*(len(code))
DP[0] = 1
DP[1] = 1

for i in range(2,len(code)):
    # 코드 숫자는 1~26
    if code[i] != '0':
        DP[i] += DP[i-1]

    num = int(code[i-1])*10+int(code[i])
    if 10 <= num <= 26:
        DP[i] += DP[i-2]

    DP[i] %= MOD

print(DP[-1])