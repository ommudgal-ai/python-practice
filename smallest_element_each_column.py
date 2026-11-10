matrix = [
    [8, 3, 7],
    [4, 9, 2],
    [6, 1, 5],
    [7, 4, 8]
]
rows=len(matrix)
cols=len(matrix[0])

for i in range(cols):
    smallest_num = matrix[0][i]
    for j in range(rows):
        num=matrix[j][i]
        if num<smallest_num:
            smallest_num=num
    print("column ",i+1,":",smallest_num)
    
