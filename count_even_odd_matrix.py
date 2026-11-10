matrix = [
    [4, 8, 2, 9],
    [3, 17, 5, 1],
    [6, 2, 10, 4]
]
even_count=0
odd_count=0
row=len(matrix)
cols=len(matrix[0])
for i in range(row):
    for j in range(cols):
        if matrix[i][j]%2==0:
            even_count+=1
        else:
            odd_count+=1
print("Even numbers:",even_count)
print("Odd numbers:",odd_count)
