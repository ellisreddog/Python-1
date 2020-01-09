list1 = [34,56,34,26,80,57,98,10,80,64,102,35,6,87,88]
count = 0
for i in range(len(list1)):
    if list1[i] >=80 and list1[i]<=100:
        count = count + 1
print("number of ints in range 80-100",count)

for i in range(len(list1)):
    if list1[i]>=80 and list1[i] <= 100:
        item = list1[i]
        list1.remove(item)
        list1.insert(i,"")

counter = 0
while True:
    if counter == len(list1):
        break
    else:
        if list1[counter] == "":
            a = list1[counter]
            list1.remove(a)
            counter = counter + 1
        else:
            counter = counter + 1
list1.remove("")

print(list1)
    
    
