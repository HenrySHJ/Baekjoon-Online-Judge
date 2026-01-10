import sys
input = sys.stdin.readline

N = int(input())

cards = [int(input()) for _ in range(N)]
    
# 딕셔너리로 빈도수 계산
count = {}
for i in range(N):
    count[cards[i]] = count.get(cards[i],0) + 1
    
# 정렬 조건 설정
result = sorted(count.items(),key=lambda x:(-x[1],x[0]))
    
print(result[0][0])