matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
result=[]

rows=len(matrix)
cols=len(matrix[0])

for i in range(cols):
    temp=[]
    for j in range(rows):
        temp.append(matrix[j][i])
    result.append(temp)
print(result)
