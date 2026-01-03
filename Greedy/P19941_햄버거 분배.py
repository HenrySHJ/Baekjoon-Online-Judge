import sys
input = sys.stdin.readline

N,K = map(int,input().split())
HP = list(input().strip())
    
count = 0
    
for i in range(N):
    if HP[i] == 'P':
        start = max(0, i-K)
        end = min(N, i+K+1)
        
        # 햄버거 찾으면 표시 남기고 바로 break
        for j in range(start, end):
            if HP[j] == 'H':
                HP[j] = 'X'
                count += 1
                break
                    
print(count)