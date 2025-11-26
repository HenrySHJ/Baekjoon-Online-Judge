import sys
input = sys.stdin.readline

while True:
    case = 1
    L,P,V = map(int,input().split())

    if L == 0 and P == 0 and V == 0:
        break
    
    ans = 0
    date = 0
    
    while date + P < V:
        ans += L
        date += P

    ans += min(V-date,L)

    print("Case",str(case)+":",ans)
    case += 1