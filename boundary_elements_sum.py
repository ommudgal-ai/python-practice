matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
rows=len(matrix)
cols=len(matrix[0])
sum=0
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            sum+=matrix[i][j]
print(sum)
