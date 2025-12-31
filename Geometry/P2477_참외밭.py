import sys
input = sys.stdin.readline

K = int(input())

edges = [list(map(int,input().split()))[1] for _ in range(6)]

max_area = 0
sub_area = 0
idx = 0

for i in range(6):
    cur_area = edges[i]*edges[(i+1)%6]
    if cur_area > max_area:
        max_area = cur_area
        idx = i

sub_area = edges[(idx+3)%6] * edges[(idx+4)%6]

print((max_area-sub_area)*K)