ans = 0

res = [10**i for i in range(10)]

for i in range(3):
    color = input()

    if i != 2:
        if color == 'black':
            ans = ans*10 + 0
        elif color == 'brown':
            ans = ans*10 + 1
        elif color == 'red':
            ans = ans*10 + 2
        elif color == 'orange':
            ans = ans*10 + 3
        elif color == 'yellow':
            ans = ans*10 + 4
        elif color == 'green':
            ans = ans*10 + 5
        elif color == 'blue':
            ans = ans*10 + 6
        elif color == 'violet':
            ans = ans*10 + 7
        elif color == 'grey':
            ans = ans*10 + 8
        elif color == 'white':
            ans = ans*10 + 9

    else:   
        if color == 'black':
            ans *= res[0]
        elif color == 'brown':
            ans *= res[1]
        elif color == 'red':
            ans *= res[2]
        elif color == 'orange':
            ans *= res[3]
        elif color == 'yellow':
            ans *= res[4]
        elif color == 'green':
            ans *= res[5]
        elif color == 'blue':
            ans *= res[6]
        elif color == 'violet':
            ans *= res[7]
        elif color == 'grey':
            ans *= res[8]
        elif color == 'white':
            ans *= res[9]
    
print(ans)