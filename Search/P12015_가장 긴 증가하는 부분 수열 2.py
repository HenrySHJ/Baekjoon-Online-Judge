import sys
input = sys.stdin.readline

# 이분 탐색
def binarySearch(lst, start, end, target):
    if start == end:
        lst[start] = target
        return
    
    mid = (start + end) // 2

    if target <= lst[mid]:
        binarySearch(lst, start, mid, target)
    else:
        binarySearch(lst, mid + 1, end, target)

N = int(input())
A = list(map(int, input().split()))

# 가장 긴 증가하는 부분 수열
LIS = [A[0]]

for i in range(1, N):
    # 현재 원소가 LIS의 마지막 값보다 크면 그대로 추가
    if A[i] > LIS[-1]:
        LIS.append(A[i])

    # 제외하고는 이분 탐색
    else:
        binarySearch(LIS, 0, len(LIS) - 1, A[i])

print(len(LIS))