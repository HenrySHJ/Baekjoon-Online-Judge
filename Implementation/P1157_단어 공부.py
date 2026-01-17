word = list(input())

alphabet = {}
for alp in word:
    if ord(alp) >= 97:
        alp = chr(ord(alp)-32)
    alphabet[alp] = alphabet.get(alp,0) + 1

lst = sorted(alphabet.items(),key=lambda x : x[1])

if len(lst) == 1 or lst[-1][1] != lst[-2][1]:
    print(lst[-1][0])
else:
    print("?")