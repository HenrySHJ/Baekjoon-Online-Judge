import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    trie = {}
    check = True 
    for _ in range(N):
        num = list(input().strip())
        
        # 무일관성으로 판정이 이미 난 경우
        if not check:
            continue

        # 딕셔너리로 트라이 형태 구현
        cur = trie
        for n in num:
            # 다른 번호가 접두사가 되는 경우
            if '*' in cur:
                check = False
                break
            
            # 트라이 확장
            elif n not in cur:
                cur[n] = {}
            cur = cur[n]
        

        # 현재 번호가 접두사
        if cur:
            check = False

        # 종료 마커
        cur['*'] = True
            
    if check:
        print("YES")
    else:
        print("NO")