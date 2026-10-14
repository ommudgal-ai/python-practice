nums = [10, 20, 30, 40, 50, 60, 70]
target =60
low=0
high=len(nums)-1
while low<=high:
    mid=(low+high)//2
    if target>nums[mid]:
        low=mid+1
    elif target<nums[mid]:
        high=mid-1
    elif target==nums[mid]:
        print(mid)
        break
else:
    print(-1)
