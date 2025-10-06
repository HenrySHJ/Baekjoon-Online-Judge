N = int(input())

case = []
case.append((1,0))
case.append((0,1))

for i in range(2,41):
    a = case[i-1][0] + case[i-2][0]
    b = case[i-1][1] + case[i-2][1]
    case.append((a,b))

for _ in range(N):
    M = int(input())
    print(*case[M])