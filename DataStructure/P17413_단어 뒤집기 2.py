word = list(input())

stack = []
isOpen = False

for i in range(len(word)):
    if word[i] == '<':
        while stack:
            print(stack.pop(), end = "")

        isOpen = True
        stack.append(word[i])

    elif word[i] == '>':
        stack.append(word[i])
        for j in range(len(stack)):
            print(stack[j], end = "")
            
        isOpen = False
        stack = []

    elif word[i] == " ":
        if not isOpen:
            while stack:
                print(stack.pop(), end = "")
            print(end = " ")
        else:
            stack.append(word[i])

    else:
        stack.append(word[i])

while stack:
    print(stack.pop(), end = "")