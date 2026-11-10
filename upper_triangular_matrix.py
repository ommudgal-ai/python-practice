matrix = [
    [1, 2, 3],
    [0, 5, 6],
    [0, 0, 9]
]

row=len(matrix)
cols=len(matrix[0])
found=True
if row!=cols:
    print("not upper trangular matrix")
else:
    for i in range(row):
        for j in range(cols):
            if i>j and matrix[i][j]!=0:
                found=False
                break
    if found:
        print("upper triangular matrix")
    else:
        print("not upper trianguar matrix")
