list1 = [2,5,15,36,47,56,59,78,244,268]
list2 = [18,39,42,43,66,69,100]
merge_list = []

for i in range(len(list1)):
    merge_list.append(list1[i])
for i in range(len(list2)-1):
    for x in range(len(merge_list)-1):
        if len(merge_list) == x:
            merge_list.instert(x,list2[i])
        if list2[i] > merge_list[x]:
            if list2[i] < merge_list[x+1]:
                merge_list.insert(x+1,list2[i])
                break
print(list1)
print(list2)
print(merge_list)
