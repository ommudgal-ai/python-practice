nums = [1, 3, 4, 2, 3]
set=[]
for i in range(len(nums)):
    if nums[i] in set:
        print(nums[i])
        break
    else:
        set.append(nums[i])
