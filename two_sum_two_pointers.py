nums = [1, 2, 3, 4, 6]
target = 7
left=0
right=len(nums)-1
while left<right:
    if nums[left]+nums[right]==target:
        print(f"({nums[left]}, {nums[right]})")
        right-=1
        left+=1
    elif nums[left]+nums[right]>target:
        right-=1
    elif nums[left]+nums[right]<target:
        left+=1
