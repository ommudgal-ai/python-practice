nums = [2, 5, 1, 8, 3]
a=0
b=1
greatest_sum=nums[a]+nums[b]
for i in range(len(nums)-1):
    if nums[a]+nums[b]>greatest_sum:
        greatest_sum=nums[a]+nums[b]
    a+=1
    b+=1
    
print(greatest_sum)
