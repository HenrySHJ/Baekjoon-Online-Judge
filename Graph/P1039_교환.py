import sys
input = sys.stdin.readline
from collections import deque

N,K = map(int,input().split())
s = str(N)     # 문자열 상태로 변환
length = len(s)

# 한 자리수 예외처리
if length == 1:
    print(-1)
    exit()

queue = {s} 

for _ in range(K):
    next_set = set()
    for num in queue:
        arr = list(num)
        for i in range(length):
            for j in range(i+1, length):
                arr[i], arr[j] = arr[j], arr[i]
                if arr[0] != '0':         # 0이 앞으로 오는 경우(leading zero) 방지
                    next_set.add(''.join(arr))
                arr[i], arr[j] = arr[j], arr[i]
    queue = next_set
    if not queue:
        print(-1)
        exit()

print(max(queue))