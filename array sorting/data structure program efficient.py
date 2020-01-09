list1 = [2,5,15,36,47,56,59,78,244,268]
list2 = [18,39,42,43,66,69,100]
list3 = []
list3 = list1
for i in range(len(list2)-1):
    list3.append(list2[i])
list3.sort()
print(list1)
print(list2)
print(list3)
