def target_element(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


print(target_element([1, 2, 3, 4, 5], 3))
print(target_element([1, 2, 3, 4, 5], 6))
