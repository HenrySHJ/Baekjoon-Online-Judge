word = input()

check = True
for i in range(len(word) // 2 + 1):
    if word[i] != word[len(word) - 1 - i]:
        check = False
        break

if check:
    print(1)
else:
    print(0)