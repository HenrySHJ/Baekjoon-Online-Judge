import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

fruits = [0] + list(map(int,input().split()))
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# DFS
def DFS(start):
    stack = [(start, -1, fruits[start])]
    best_node = start
    best_sum = fruits[start]

    while stack:
        node, parent, total = stack.pop()

        # 최대 열매 경로 업데이트
        if total > best_sum or (total == best_sum and node < best_node):
            best_sum = total
            best_node = node

        for next in tree[node]:
            if next != parent:
                stack.append((next, node, total + fruits[next]))

    return best_node, best_sum

A, _ = DFS(1)
B, max_sum = DFS(A)
start_node = min(A, B)

print(max_sum,end=' ')
print(start_node)