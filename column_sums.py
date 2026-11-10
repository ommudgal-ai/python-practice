matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rows=len(matrix)
cols=len(matrix[0])

for i in range(cols):
    sum=0
    for j in range(rows):
        sum+=matrix[j][i]
    print("column ",i+1,":",sum)
