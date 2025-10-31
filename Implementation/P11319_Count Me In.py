S = int(input())

vowels = ['A','E','I','O','U','a','e','i','o','u']
for _ in range(S):
    sent = list(input())
    v = 0
    length = 0

    for i in range(len(sent)):
        if sent[i] == ' ':
            continue
        length += 1
        for j in range(10):
            if sent[i] == vowels[j]:
                v += 1
                break
    c = length - v

    print(c,v)