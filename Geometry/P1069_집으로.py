X, Y, D, T = map(int, input().split())
dist = (X**2+Y**2)**0.5

# 걷기만 하는 경우
ans = dist

if D > T:
    # 점프가 걷기보다 빠른 경우에만 점프 고려
    jump_cnt = dist // D
    
    # dist >= D인 경우
    if dist >= D:
        # jump_cnt번 점프 후 남은 거리 걷기
        ans = min(ans, jump_cnt*T + (dist - jump_cnt * D))

        # (jump_cnt + 1)번 점프 후 되돌아오기
        ans = min(ans, (jump_cnt + 1)*T + (D*(jump_cnt + 1) - dist))

        # (jump_cnt + 1)번 점프만으로 가기 (꺾어서 가기)
        ans = min(ans, (jump_cnt + 1)*T)
        
    # dist < D인 경우
    else:
        # 한 번 점프 후 되돌아오기
        ans = min(ans, T + (D - dist))
        # 두 번 점프해서 도착 (삼각형 경로)
        ans = min(ans, 2.0*T)
        
else:
    pass

print(ans)