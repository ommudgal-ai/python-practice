nums = [1, 2, 2, 3, 3, 3, 2, 2]
number=nums[0]
count=0
max_number=nums[0]
maxi=0
for i in nums:
    if i==number:
        count+=1
    
    else:
        number=i
        count=1
    if count>maxi:
        maxi=count
        max_number=i
    
print("Number=",max_number)
print("Count=",maxi)
