import sys
input = sys.stdin.readline

N = int(input())

A = list(input().strip())
B = list(input().strip())

def switch(bulb,v):
    for i in [v-1, v, v+1]:
        if 0 <= i < N:
            bulb[i] = '1' if bulb[i] == '0' else '0'

def sol(first):
    ans = 0
    temp = A[:]
    if first:
        switch(temp,0)
        ans += 1
        
    for i in range(1,N):
        if temp[i-1] != B[i-1]:
            switch(temp,i)
            ans += 1

    if temp == B:
        return ans
    else:
        return sys.maxsize
    
ans = min(sol(False),sol(True))
print(ans if ans != sys.maxsize else -1)