MAX = 123456*2

case = [0]*(MAX+1)
S = [0]*(MAX+1)

for i in range(2,len(case)):
    case[i] = i

for i in range(2,int(MAX**0.5)+1):
    if case[i] == 0:
        continue
    else:
        for j in range(i*i,MAX+1,i):
            case[j] = 0

for i in range(2,len(case)):
    if case[i] != 0:
        S[i] = S[i-1] + 1
    else:
        S[i] = S[i-1]

while True:
    N = int(input())
    if N == 0:
        break

    print(S[N*2]-S[N])

