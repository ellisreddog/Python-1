cfound = False
rows = int(input("how many rows?"))
col = int(input("how many coloumns"))
a = ""        

Grid = [0] * rows
for i in range(rows):
    Grid[i] = [" ▄▄▄▄▄▄▄ "] * col
reg = ""
def parksacar(reg):
    while len(reg)==0 or len(reg)>7:
        reg = input("Input your Registratoin number :: ")
        if len(reg)<7:
            z = 7 - len(reg)
            for i in range(z):
                reg = reg + " "
        elif len(reg)>7:
            print("that registration plate is too long!")
    reg = "  " + reg
        
    space_found = False
    while space_found == False:
        yloc = False
        xloc = False
        while yloc == False:    
            y = int(input("What row do you want to park in? :: "))
            y = y - 1
            if y<0:
                print("choose a higher number!")
            else:
                if y>rows:
                    print("That row doesnt exist")
                else:
                    yloc = True
                
        while xloc == False:     
            x = int(input("what coloumn do you want to park in? :: "))
            x = x - 1
            if x < 0:
                print("choose a higher number!")
            else:
                if x > col:
                    print("That column doesnt exist")
                else:
                    xloc = True
            
        if Grid[x][y] == " ▄▄▄▄▄▄▄ ":
            print("All done!!")
            Grid[x][y] = reg
            space_found = True
        else:
            print("Thats been taken, sorry , Try again")
    return Grid


def findacar():
    reg = input("Input your Registration number :: ")
    for i in range(rows):
        for x in range(col):
            if reg == Grid[i][x]:
                print("found in location", x+1,",", i+1)
                cfound = True
    if cfound == False:
        print("car not found")
    
start = True
while start == True:

    choose = input(" [f] : find a car  [p] : park [v] : view :: ")
    if choose == "f":
        findacar()
    elif choose == "p":
        parksacar(reg)
    elif choose == "v":
        w = str(rows)
        for i in range(rows):
            q = ""
            
            for x in range(len(w)):
                q = q + " "
            e = list(q)
            for z in range(len(str(i+1))):
                e.remove(e[0])
            q = "".join(e)
                
    
            print("[",i+1,"]",q, " ","".join(Grid[i]))
    end = input(" [y] : yes  [n] : no, do you want to finish? ::" )
    if end == "y":
        start = False
    else:
        pass
    
