matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result=[]

rows=len(matrix)
cols=len(matrix[0])

for i in range(cols):
    temp=[]
    for j in range(rows-1,-1,-1):
        temp.append(matrix[j][i])
    result.append(temp)
print(result)
