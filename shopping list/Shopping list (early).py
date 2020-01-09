weeka = ["apple","banana","car","juice","house"]
weekb = ["apple","tractor","juice","the bee movie","shrek merch"]
weekone = False
unique = []

for i in range(len(weeka)):
    if weekb[i] in weeka:
        pass
    else:
        print(weekb[i])
        unique.append(weekb[i])
        
for i in range(len(weeka)):
    unique.append(weeka[i])

print(",".join(unique))


