nums = [4, 2, 4, 3, 2, 4, 2, 2]
frequency={}
value=0
number=0
for i in range(len(nums)):
    if nums[i] in frequency:
        frequency[nums[i]]=frequency[nums[i]]+1
    else:
        frequency[nums[i]]=1
for i in frequency:
    if frequency[i]>value:
        value=frequency[i]
        number=i
print(number)
