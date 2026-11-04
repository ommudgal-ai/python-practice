nums = [2, 1, 5, 1, 3, 2]
k = 3
if len(nums) == 0:
    print("List is empty")
elif k <= 0:
    print("Window size must be positive")
elif k > len(nums):
    print("Window size cannot exceed list length")
else:
    max_sum = 0
    for i in range(len(nums) - k + 1):
        total = 0
        for j in range(k):
            total += nums[i + j]
        if i == 0 or total > max_sum:
            max_sum = total
    print(max_sum)
