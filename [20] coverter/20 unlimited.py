squarelist = []
hexxx = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
values = []
binaryy = []
j = []
num = 0
g = 0
hexx = 0
binn = ""
done = False

def binary(inp,values):
    a = bin(inp)
    b = list(a)
    b.remove("b")
    b.remove("0")

    c = hex(inp)
    d = list(c)
    d.remove("x")
    d.remove("0")
    values.append(b)
    values.append(d)
    return values


def hextoden(a,values,g):
    c = 0
    a.reverse()
    for i in range(0,len(a)):
        b = hexxx.index(a[i])
        c = 16**i
        d = b*c
        g = g+d
    values.append(g)
    c = bin(g)
    d = str(c)
    d = list(d)
    d.remove("b")
    d.remove("0")
    values.append(d)
    return values
    


def btohd(j,num,values):
    j.reverse()

    for i in range(0,len(j)):
        if j[i] == "1":
            num = num + 2**i
        elif j[i] == "0":
            num = num + 0

    hexvalue = hex(num)
    b = list(hexvalue)
    b.remove("x")
    b.remove("0")
    values.append(num)
    values.append(b)
    return values

while done == False:

    print("B: Binary H: Hexadecimal D: Denary")
    choice = input("what would you like to convert?")

    if choice == "d":
        inp = int(input("what value would you like to convert? "))
        print("h: hexadecimal   b: binary")
        borh = input("would you like to convert it into? ")
        if borh == "b":
            binary(inp,values)
            print(values[0])
        elif borh == "h":
            binary(inp,values)
            print(values[1])

    elif choice == "h":
        hh = input("input yor hex value here: ")
        a =list(hh)
        print("d: denary b: binary")
        bord = input("what would you like to convert it into?..")
        if bord == "d":
            hextoden(a,values,g)
            print(values[0])
        elif bord == "b":
            hextoden(a,values,g)
            print(values[1])

    elif choice == "b":
        binn = input("binary: ")
        j = list(binn)
        print("")
        print("d: denary h: hexadecimal")
        dorh = input("what would tyou like to convert it into?  ")
        if dorh == "h":
            btohd(j,num,values)
            print(values[1])
        elif dorh == "d":
            btohd(j,num,values)
            print(values[0])
    print("y = YES n = NO")
    again = input("do you want to start again?")
    if again == "y":
          print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
          print("")
          values = []
          binaryy = []
          j = []
    elif again == "n":
          done  = True
