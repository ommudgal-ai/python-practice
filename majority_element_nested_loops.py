nums = [2, 3, 2, 2, 5, 2, 2]
found=False
n=len(nums)/2
for i in range(len(nums)):
    count=0
    for j in range(len(nums)):
        if nums[j]==nums[i]:
            count+=1
    if count>n:
        print(nums[i])
        found=True
        break
if not found:
    print("no majority element exist")
