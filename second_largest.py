nums = [4, 7, 2, 9, 5, 9, 1]
if nums[0]>nums[1]:
    largest=nums[0]
    slargest=nums[1]
else:
    largest=nums[1]
    slargest=nums[0]
for i in range(len(nums)):
    if nums[i]>largest:
        slargest=largest
        largest=nums[i]
    elif nums[i]>slargest and nums[i]<largest:
        slargest=nums[i]
print(slargest)
