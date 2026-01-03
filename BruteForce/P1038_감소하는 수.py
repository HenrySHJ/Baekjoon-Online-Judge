import sys
input = sys.stdin.readline

N = int(input())

# 9876543210보다 크면 -1출력
if N > 1022:
    print(-1)
    sys.exit()
    
result = []
    
def DFS(num):
    result.append(num)
        
    # 감소하는 수가 되도록 일의 자리 수 설정
    last_digit = num % 10
    for i in range(last_digit):
        DFS(num*10 + i)

# 시작점 : 0 ~ 9 (한자리 수)
for i in range(10):
    DFS(i)
    
# 생성된 수들을 오름차순 정렬
result.sort()
    
print(result[N])