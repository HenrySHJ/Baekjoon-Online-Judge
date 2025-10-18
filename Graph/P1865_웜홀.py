TC = int(input())

def bellman_ford():
    time = [0]*(N+1)
    for i in range(N):
        for s, e, t in road:
            if time[e] > time[s] + t:
                time[e] = time[s] + t
                if i == N-1:
                    return "YES"  # 마지막까지도 계속해서 갱신이 되면 YES
    return "NO" # 마지막까지도 계속해서 갱신이 되면 NO

for _ in range(TC):
    N,M,W = map(int,input().split())

    road = []

    for _ in range(M):
        S,E,T = map(int,input().split())
        road.append((S,E,T))
        road.append((E,S,T))

    for _ in range(W):
        S,E,T = map(int,input().split())
        road.append((S,E,-T))

    print(bellman_ford())
    