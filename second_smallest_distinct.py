nums = [8, 3, 5, 1, 3, 2, 1, 6]
set1 = set(nums)

if len(set1) < 2:
    print("Second smallest number does not exist")
else:
    smallest = float('inf')
    ssmallest = float('inf')

    for i in set1:
        if i < smallest:
            ssmallest = smallest
            smallest = i
        elif i < ssmallest:
            ssmallest = i

    print(ssmallest)
