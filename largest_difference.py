nums = [4, 7, 2, 9, 5, 1]
if nums[0]>nums[1]:
    largest=nums[0]
    smallest=nums[1]
else:
    smallest=nums[0]
    largest=nums[1]
for i in nums:
    if i>largest:
        largest=i
for i in nums:
    if i<smallest:
        smallest=i
print("Maximum difference is ",largest-smallest)
