matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
rows=len(matrix)
cols=len(matrix[0])
is_identity=True
if rows!=cols:
    print("given matrix is not identity matrix")
else:

    for i in range(rows):
        for j in range(cols):
            if i==j and matrix[i][j]!=1:
                is_identity=False
            elif i!=j and matrix[i][j]!=0:
                is_identity=False
    if is_identity==True:
        print("Given matrix is identity matrix")
    else:
        print("given matrix is not identity matrix")
