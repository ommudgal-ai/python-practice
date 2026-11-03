nums = [8, 1, 5, 12, 3, 9]
difference=abs(nums[0]-nums[1])
a=nums[0]
b=nums[1]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if abs(nums[i]-nums[j])<difference:
            difference=abs(nums[i]-nums[j])
            a=nums[i]
            b=nums[j]
print(a,b)
print("smallest difference=",difference)
