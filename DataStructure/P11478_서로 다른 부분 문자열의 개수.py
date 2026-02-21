S = input()

dict_S = {}

for i in range(len(S) + 1):
    for j in range(i):
        if dict_S.get(S[j:i], 0) == 0:
            dict_S[S[j:i]] = 1

print(len(dict_S))