import sys
input = sys.stdin.readline

S = list(input().strip())

dict = {}

for alphabet in S:
    dict[alphabet] = dict.get(alphabet,0) + 1

odd = 0
for key in dict:
    if dict[key] % 2 == 1:
        odd += 1

if len(S) % 2 == 0 and odd > 0:
    print("I'm Sorry Hansoo")

elif len(S) % 2 == 1 and odd > 1:
    print("I'm Sorry Hansoo")

else:
    ans = ['']*len(S)
    dicts = sorted(dict.items())

    i = 0
    mid = len(S)//2
    for a,b in dicts:
        if b % 2 == 1:
            ans[mid] = a
        for _ in range(b//2):
            ans[i] = a
            ans[len(S)-1-i] = a
            i += 1

    for i in range(len(S)):
        print(ans[i],end='')