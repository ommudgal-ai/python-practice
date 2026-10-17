nums = [1, 2, 2, 3, 3, 3, 4, 4]
freq={}
lvalue = 0
slvalue = 0

for i in range(len(nums)):
    if nums[i] in freq:
        freq[nums[i]]+=1
    else:
        freq[nums[i]]=1

for i in freq:
    if freq[i]>lvalue:
        slvalue=lvalue
        lvalue=freq[i]
        number=i
    elif freq[i]<lvalue and slvalue<freq[i]:
        slvalue=freq[i]
        number=i
    elif freq[i]==slvalue:
        number=i
for i in nums:
    if freq[i]==slvalue:
        print(i)
        break
