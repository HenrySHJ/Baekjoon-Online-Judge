import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
name = list(input().split())

tree = {}
indegree = {}
kids = {}

for i in range(N):
    tree[name[i]] = []
    indegree[name[i]] = 0
    kids[name[i]] = []

M = int(input())
for _ in range(M):
    x,y = input().split()

    tree[y].append(x)
    indegree[x] += 1

queue = deque()
ancestor = []

for i in range(N):
    if indegree[name[i]] == 0:
        queue.append(name[i])
        ancestor.append(name[i])

# 초기 queue 길이 -> 가문 수
print(len(queue))
ancestor.sort()

for anc in ancestor:
    print(anc,end=' ')
print()

while queue:
    now = queue.popleft()

    for next in tree[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            kids[now].append(next)
            queue.append(next)

kids = sorted(kids.items())

for key in kids:
    key[1].sort()
    print(key[0],len(key[1]),*key[1])