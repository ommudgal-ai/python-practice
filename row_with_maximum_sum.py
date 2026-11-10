matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 1, 2],
    [3, 8, 4]
]
rows=len(matrix)
cols=len(matrix[0])
sum=0
for i in range(rows):
    temp_summ=0
    for j in range(cols):
        temp_summ+=matrix[i][j]
    if temp_summ>sum:
        sum=temp_summ
        roww=i
print("Row", roww+1, "has the maximum sum:", sum)
