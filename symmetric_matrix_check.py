matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
rows=len(matrix)
cols=len(matrix[0])
is_symmetric=True
if rows!=cols:
    print("given matrix is not symmetric matrix")
else:

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]!=matrix[j][i]:
                is_symmetric=False
    if is_symmetric:
        print("given matrix is symmetric matrix")
    else:
        print("given matrix is not symmetric matrix")
