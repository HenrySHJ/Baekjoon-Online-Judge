while True:
    try:
        A,B = map(int,input().split())
        if A < 10 and B < 10:
            print(A+B)
        else:
            break
    except:
        if EOFError or ValueError:
            break