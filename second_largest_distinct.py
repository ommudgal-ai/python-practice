nums = [12, 5, 8, 12, 10, 8, 7]

largest = nums[0]
slargest = None

for i in nums:
    if i > largest:
        slargest = largest
        largest = i
    elif i < largest:
        if slargest is None or i > slargest:
            slargest = i

print(slargest)
