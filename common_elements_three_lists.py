list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 5, 7]
list3 = [2, 5, 8, 9]
for i in list1:
    if i in list2 and i in list3:
        print(i)
