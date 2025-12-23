import sys
input = sys.stdin.readline

N,M = map(int,input().split())

unseen = {input().strip() for _ in range(N)}
unheard = {input().strip() for _ in range(M)}

result = sorted(list(unheard & unseen))
    
print(len(result))

for name in result:
    print(name)