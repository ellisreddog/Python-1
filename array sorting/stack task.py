end = False

while end == False:

    word = input("input word/words: ")
    stack = [" "] * len(word)
    b = list(word)

    head = 0
    tail = len(stack)-1


    for i in range(len(stack)):
        stack[tail] = b[head]
        tail = tail - 1
        head = head + 1
        print(stack)

    if stack == b:
        print("palendrome")
    else:
        print("nah")
    fin = input("do you want to go again y/n")
    if fin == "y":
        pass
    elif fin == "n":
        end = True
        


