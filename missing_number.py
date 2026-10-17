nums = [1, 2,4, 5, 6]
n=1
for i in range(len(nums)):
    if nums[i]==n:
        n=n+1
    else:
        print(n)
        break
