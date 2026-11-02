nums = [1, 2, 3, 2, 4, 5, 3, 6, 1]
set1=set()
for i in nums:
    if i in set1:
        print(i)
    else:
        set1.add(i)
