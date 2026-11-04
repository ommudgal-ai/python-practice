nums = [1, 2, 1, 3, 4, 2, 3]
k = 4
if len(nums)==0:
    print("list is empty")
elif k<=0:
    print("window size must be positive")
elif k>len(nums):
    print("window size cannot exceed list length")
else:
    for i in range(len(nums)-k+1):
        set1=set()

        for j in range(k):
            set1.add(nums[i + j])
        print(len(set1))
