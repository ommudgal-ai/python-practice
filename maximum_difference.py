nums = [7, 1, 5, 3, 6, 4]

smallest=nums[0]
max_diff=0
for n in nums:
    if n<smallest:
        smallest=n
    if n-smallest>max_diff:
        max_diff=n-smallest
print("maximum difference is: ",max_diff)
