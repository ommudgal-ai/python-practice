matrix = [
    [4, 2, 7],
    [3, 5, 1],
    [8, 6, 9]
]
rows=len(matrix)
cols=len(matrix[0])
primary_sum=0
secondary_sum=0
for i in range(rows):
    for j in range(cols):
        if i + j == cols - 1:
            secondary_sum+=matrix[i][j]
        if i==j:
            primary_sum+=matrix[i][j]
print("Primary diagonal sum:",primary_sum)
print("Secondary diagonal sum:",secondary_sum)
print("Difference:",abs(primary_sum - secondary_sum))
