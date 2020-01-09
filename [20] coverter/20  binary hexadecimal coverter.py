squarelist = [128,64,32,16,8,4,2,1]

hexxx = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

num = 0

g = 0
hexx = 0
binn = ""
done = False

def binary(inp,values):
    if inp > 255:
        print("inavlid")
    total = inp
    for i in range(len(squarelist)):
        if inp >= squarelist[i]:
            inp = inp - squarelist[i]
            binaryy.append("1")
        else:
            binaryy.append("0")

    c = 0
    counter = 8
    for i in range(0,8):

         if binaryy[i] == "1":
                c = c + squarelist[i]
    if total>255:
        print("invalid")
    elif total <= 255:
        a = hex(total)
        b = list(a)
        b.remove("x")
        b.remove("0")
    values.append(b)
    values.append(binaryy)
    return values


def hextoden(a,values):
    b = hexxx.index(a[0])
    b = b*16
    c = hexxx.index(a[1])
    total = 0
    total = c+b
    totala = total
    
    for i in range(len(squarelist)):
        if total >= squarelist[i]:
            total = total - squarelist[i]
            binaryy.append("1")
        else:
            binaryy.append("0")
    values.append(binaryy)
    values.append(totala)
    return values


def btohd(j,num,values):
    j = list(binn)

    if len(j) > 8 or len(j) < 8:
        print("invalid")
    else:    
        for i in range(len(j)):
            if j[i] == "1":
                num = num + squarelist[i]
            elif j[i] == "0":
                num = num + 0

    hexvalue = hex(num)
    b = list(hexvalue)
    b.remove("x")
    b.remove("0")
    values.append(b)
    values.append(num)
    return values

while done == False:
    values = []
    binaryy = []
    j = []
    print("B: Binary H: Hexadecimal D: Denary")
    choice = input("what would you like to convert?")

    if choice == "d":
        inp = int(input("what value would you like to convert? "))
        print("h: hexadecimal   b: binary")
        borh = input("would you like to convert it into? ")
        if borh == "b":
            binary(inp,values)
            print(binaryy)
        elif borh == "h":
            binary(inp,values)
            print(values[0])

    elif choice == "h":
        hh = input("input yor hex value here: ")
        a =list(hh)
        print("d: denary b: binary")
        bord = input("what would you like to convert it into?..")
        if bord == "d":
            z = hextoden(a,values)
            print(z[1])
        elif bord == "b":
            z = hextoden(a,values)
            print(z[0])

    elif choice == "b":
        binn = input("binary: ")
        print("")
        print("d: denary h: hexadecimal")
        dorh = input("what would tyou like to convert it into?  ")
        if dorh == "h":
            g = btohd(j,num,values)
            print(g[0])
        elif dorh == "d":
            g = btohd(j,num,values)
            print(g[1])
    print("y = YES n = NO")
    again = input("do you want to start again?")
    if again == "y":
          print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
          print("")
    elif again == "n":
          done  = True
