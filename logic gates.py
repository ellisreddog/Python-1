print(" OR, AND, XOR, NAND and NOR")
inn = input("choose a gate")
inputa = int(input("1/0 :"))
inputb = int(input("1/0 :"))
    


def OR(inputa,inputb):
    if inputa == 1 or inputb == 1:
        output = 1
    else:
        output = 0
    return output


def AND(inputa,inputb):
    if inputa and inputb == 1:
        output = 1
    else:
        output = 0
    return output

def XOR(inputa,inputb):
    if inputa == 1 and inputb == 0:
        output = 1
    elif inputa == 0 and inputb == 1:
        output = 1
    else:
        output = 0
    return output


if inn == "OR":
    print(OR(inputa,inputb))
if inn == "XOR":
    print(XOR(inputa,inputb))
if inn == "AND":
    print(AND(inputa,inputb))
if inn == "NAND":
     a = AND(inputa,inputb)
     if a == 1:
         print("0")
     elif a == 0:
        print("1")
if inn == "NOR":
    a = OR(inputa,inputb)
    if a == 0:
        print("1")
    elif a == 1:
        print("0")
    

