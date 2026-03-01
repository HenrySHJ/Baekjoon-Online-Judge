import sys
input = sys.stdin.readline

T = int(input())

# 이분 매칭
def DFS(now):
    for nxt in graph[now]:
        if visited[nxt]:
            continue

        visited[nxt] = True

        if matched[nxt] == -1 or DFS(matched[nxt]):
            matched[nxt] = now
            return True
        
    return False

for _ in range(T):
    C, D, V = map(int, input().split())

    # 선호하는 동물에 따라 투표끼리 분류
    vote_cat = []
    vote_dog = []
    ans = 0

    for i in range(1, V + 1):
        # 투표 입력받기
        vote = list(input().split())

        # 고양이를 선호하는 경우
        if vote[0][0] == 'C':
            vote_cat.append((int(vote[0][1:]), int(vote[1][1:])))

        # 개를 선호하는 경우
        elif vote[0][0] == 'D':
            vote_dog.append((int(vote[0][1:]), int(vote[1][1:])))

    # 각 동물에 따른 선호 수
    vote_cat_count = len(vote_cat)
    vote_dog_count = len(vote_dog)

    # 상충되는 투표 확인해서 인접 그래프로 옮기기
    graph = [[] for _ in range(vote_cat_count)]

    # 충돌하는 투표에 대해 간선을 생성하기
    for i in range(vote_cat_count):
        for j in range(vote_dog_count):
            if (vote_cat[i][1] == vote_dog[j][0] or vote_cat[i][0] == vote_dog[j][1]):
                graph[i].append(j)

    # 연결 여부 확인하기
    matched = [-1] * vote_dog_count
    unmatched = 0

    for i in range(vote_cat_count):
        visited = [False] * vote_dog_count

        if DFS(i):
            unmatched += 1

    print(V - unmatched)