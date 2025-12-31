D,H,W = map(int,input().split())

i = (D**2/(H**2 + W**2))**0.5

print(int(i*H),int(i*W))