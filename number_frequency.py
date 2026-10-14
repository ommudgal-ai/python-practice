nums = [2, 3, 2, 5, 3, 2, 1]
frequency={}
for i in range(len(nums)):
    if nums[i] in frequency:
        frequency[nums[i]]=frequency[nums[i]]+1
    else:
        frequency[nums[i]]=1
print(frequency)
