matrix = [
    [1, 0, 0],
    [4, 5, 0],
    [7, 8, 9]
]

row=len(matrix)
cols=len(matrix[0])
found=True
if row!=cols:
    print("not lower trangular matrix")
else:
    for i in range(row):
        for j in range(cols):
            if i<j and matrix[i][j]!=0:
                found=False
                break
    if found:
        print("lower triangular matrix")
    else:
        print("not lower trianguar matrix")
