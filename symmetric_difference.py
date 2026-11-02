list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1=set(list1)
set2=set(list2)
for i in range(len(list1)):
    if list1[i] not in set2:
        print(list1[i])
for i in range(len(list2)):
    if list2[i] not in set1:
        print(list2[i])
