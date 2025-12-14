import sys
input = sys.stdin.readline

N = int(input())
trie = {}

for _ in range(N):
    data = input().split()
    cur = trie

    # idx 1부터 정보시작
    for x in data[1:]:
        if x not in cur:
            cur[x] = {}
        cur = cur[x]
        
def DFS(node, depth):
    for key in sorted(node):
        print("--" * depth + key)
        DFS(node[key], depth + 1)

DFS(trie, 0)