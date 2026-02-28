A, B, C, M = map(int, input().split())

fatigue = 0
work = 0
time = 0

while time < 24:
    time += 1

    if fatigue + A <= M:
        fatigue += A
        work += B
        
    else:
        fatigue = max(0, fatigue - C)

print(work)