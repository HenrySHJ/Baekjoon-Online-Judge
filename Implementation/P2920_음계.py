note = list(map(int, input().split()))

check = 0
if note[0] > note[1]:
    check = 1

for i in range(1,7):
    if note[i] < note[i + 1]:
        if check == 0:
            continue
        else:
            check = 2
            break
    
    elif note[i] > note[i + 1]:
        if check == 1:
            continue
        else:
            check = 2
            break

if check == 0:
    print("ascending")
elif check == 1:
    print("descending")
else:
    print("mixed")