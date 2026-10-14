nums = [2, 4, 6, 8, 10]
left = 0
right = len(nums) - 1
while left<right:
    nums[left],nums[right]=nums[right],nums[left]
    left+=1
    right-=1
print(nums)
