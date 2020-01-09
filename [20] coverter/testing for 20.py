##binary to hex and binary to den
a = []
squarelist = [128,64,32,16,8,4,2,1]
num = 0
inp = input("")
values = []

def btohd(a,num,values):
    a = list(inp)

    if len(a) > 8 or len(a) < 8:
        print("invalid")
    else:    
        for i in range(len(a)):
            if a[i] == "1":
                num = num + squarelist[i]
            elif a[i] == "0":
                num = num + 0


    hexvalue = hex(num)
    b = list(hexvalue)
    b.remove("x")
    b.remove("0")
    values.append(b)
    values.append(num)
    return values
    
    

g = btohd(a,num,values)

print(g[0])

