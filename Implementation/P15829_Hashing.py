L = int(input())
word = list(input())

ans = 0
for i in range(L):
    w = word[i]
    ans += (ord(w) - ord('a') + 1) * 31 ** i

print(ans)