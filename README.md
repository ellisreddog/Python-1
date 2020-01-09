fruits = ["cherry","bell","lemon","orange","star","skull"]
credit = 100
import random
import time
start = False
roll = False
game = False


while game == False:
    print("")
    
    if credit == 0 or credit < 0:
        break
    while start == False:
        print("20 credits to play")
        begin = input("press enter to start or type 'quit' to end")
        if begin == "quit":
            print("final balance:",credit)
            game = True
        else:
            print("20 credits removed to play")
            start = True
            roll = True
            
            


    while roll == True:
        
        credit = credit - 20

        slot = fruits[random.randint(0,5)]
        slot2 = fruits[random.randint(0,5)]
        slot3 = fruits[random.randint(0,5)]
        print("")
        print(slot)
        time.sleep(0.5)
        print(slot2)
        time.sleep(0.5)
        print(slot3)
        time.sleep(0.5)
        print("")
        if slot == slot2 and slot2 == "skull" and slot != slot3 or slot2 == slot3 and slot2 == "skull" and slot2 != slot or slot == slot3 and slot == "skull" and slot != slot2:
            credit = credit - 100
            print("LOST £1")
            roll = False

        elif slot == slot2 and slot2 == slot3 and slot2 == "skull":
            credit = 0
            roll = False
            game = True

        elif slot == slot2 and slot2 == slot3 and slot == "bell":
            print("MEGA JACKPOT")
            credit = credit + 500
        elif slot == slot2 and slot2 == slot3:
            print("JACKPOT    + £1")
            credit = credit + 100                    
        elif slot == slot2:
            print("you win 50p")
            credit = credit + 50
        elif slot == slot3:
            print("you win 50p")
            credit = credit + 50
        elif slot2 == slot3:
            print("you win 50p")
            credit = credit + 50

        else:
            print("you lost :( ")
        roll = False
        start = False

        if credit >= 1:
            print("credit: ",credit)
        else:
            print("credit: 0")
            
        
    
print("game over")
