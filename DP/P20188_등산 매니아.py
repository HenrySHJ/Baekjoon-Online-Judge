import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

# 인접 그래프
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 노드의 하위 노드의 개수
subsize = [0]*(N+1)

ans = 0

def get_subsize(now, prev):
    global ans
    count = 1  # 자기 자신 포함
    
    for next in graph[now]:
        # 상위 방향이 아닌 경우 추가
        if next != prev:
            count += get_subsize(next, now)
        
    subsize[now] = count
        
    # 해당 간선의 사용 횟수를 구하기
    if now != 1:
        # 해당 노드 포함 하위 노드가 아닌 노드의 수
        remain = N - count

        # 전체 노드를 이용한 조합
        total = N*(N-1) // 2

        # 하위 노드를 이용하지 않고 만드는 조합
        outside_sub = remain*(remain-1) // 2

        # 조합의 차 만큼 정답에 추가
        ans += (total - outside_sub)
            
    return count

get_subsize(1, 0)

print(ans)