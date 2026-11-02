list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

set2=set(list2)
for i in range(len(list1)):
    if list1[i] in set2:
        print(list1[i])
