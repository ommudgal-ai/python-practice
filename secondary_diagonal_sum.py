matrix = [
    [2, 4, 6],
    [1, 5, 9],
    [3, 7, 8]
]
rows=len(matrix)
cols=len(matrix[0])
sum=0
for i in range(rows):
    for j in range(cols):
        if i + j == cols - 1:
            sum+=matrix[i][j]

print(sum)
