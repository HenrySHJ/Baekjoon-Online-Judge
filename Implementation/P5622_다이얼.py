word = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
total = 0

for c in word:
    for i in range(8):
        if c in dial[i]:
            total += (i + 3)
            break

print(total)