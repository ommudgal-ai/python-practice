nums = [2, 3, 2, 2, 5, 2, 2]
n=len(nums)/2
freq={}
found=None
for i in nums:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in freq:
    if freq[i]>n:
        found=i
        print(found)
if found==None:
    print("No majority element exists")
