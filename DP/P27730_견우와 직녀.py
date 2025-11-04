import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

tree1 = [[] for _ in range(N+1)]
DP1 = [0]*(N+1)
subsize1 = [0]*(N+1)
visited1 = [False]*(N+1)

for _ in range(N-1):
    a,b,c = map(int,input().split())
    tree1[a].append((b,c))
    tree1[b].append((a,c))

M = int(input())

tree2 = [[] for _ in range(M+1)]
DP2 = [0]*(M+1)
subsize2 = [0]*(M+1)
visited2 = [False]*(M+1)

for _ in range(M-1):
    a,b,c = map(int,input().split())
    tree2[a].append((b,c))
    tree2[b].append((a,c))

# 견우 DFS
def DFS1(v):
    visited1[v] = True
    subsize1[v] += 1
    for next,dist in tree1[v]:
        if visited1[next]:
            continue
        DFS1(next)
        subsize1[v] += subsize1[next]
        DP1[v] += DP1[next] + dist*(subsize1[next])

# 직녀 DFS
def DFS2(v):
    visited2[v] = True
    subsize2[v] += 1
    for next,dist in tree2[v]:
        if visited2[next]:
            continue
        DFS2(next)
        subsize2[v] += subsize2[next]
        DP2[v] += DP2[next] + dist*(subsize2[next])

# 견우 reroot
def reroot1(v):
    visited1[v] = True

    for next,dist in tree1[v]:
        if visited1[next]:
            continue
        DP1[next] = DP1[v] + dist*(N - 2*subsize1[next])
        reroot1(next)

# 직녀 reroot
def reroot2(v):
    visited2[v] = True

    for next,dist in tree2[v]:
        if visited2[next]:
            continue
        DP2[next] = DP2[v] + dist*(M - 2*subsize2[next])
        reroot2(next)

DFS1(1)
visited1 = [False]*(N+1)
reroot1(1)

DFS2(1)
visited2 = [False]*(M+1)
reroot2(1)

ans1 = 1
bridge1 = sys.maxsize
for i in range(1,N+1):
    if bridge1 >= DP1[i]:
        ans1 = i
        bridge1 = DP1[i]

ans2 = 1
bridge2 = sys.maxsize
for i in range(1,M+1):
    if bridge2 >= DP2[i]:
        ans2 = i
        bridge2 = DP2[i]

print(ans1,ans2)
print(DP1[ans1]*M + DP2[ans2]*N + N*M)