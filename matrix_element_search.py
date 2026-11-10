matrix = [
    [4, 8, 2, 9],
    [3, 7, 5, 1],
    [6, 2, 10, 4]
]
found=False
target = 7
row=len(matrix)
cols=len(matrix[0])
for i in range(row):
    for j in range(cols):
        if matrix[i][j]==target:
            found=True
            print("Element found")
            print("Row:",i+1)
            print("Column:",j+1)
if found==False:
    print("element is not present")
