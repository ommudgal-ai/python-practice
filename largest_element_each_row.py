matrix = [
    [3, 8, 2, 5],
    [9, 1, 6, 4],
    [7, 12, 5, 10]
]
rows=len(matrix)
cols=len(matrix[0])

for i in range(rows):
    highest_num=matrix[i][0]
    for j in range(cols):
        num=matrix[i][j]
        if num>highest_num:
            highest_num=num
    print("Row ",i+1,":",highest_num)
    
