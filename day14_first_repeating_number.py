nums = [5, 3, 1, 3, 5, 2]
list=[]
for i in nums:
    if i in list:
        print("number appears twice:",i)
        break
    else:
        list.append(i)
