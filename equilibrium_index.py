nums = [1, 3, 5, 2, 2]
found=False
for i in range(len(nums)):
    left=0
    right=0
    for j in range(0,i):
        left+=nums[j]
    for k in range(i+1,len(nums)):
            right+=nums[k]
    if left==right:
         found=True
         print("Equilibrium index",i)
         break
if not found:
     print("No equilibrium index found")
