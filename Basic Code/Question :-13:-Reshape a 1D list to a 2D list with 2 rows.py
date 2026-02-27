#Question :-13:-Reshape a 1D list to a 2D list with 2 rows.

numbers = [0,1,2,3,4,5,6,7,8,9]
matrix = []
row1 = []
row2 = []

for i in range(5):
    row1.append(numbers[i])

for i in range(5,10):
    row2.append(numbers[i])

matrix.append(row1)
matrix.append(row2)

print(matrix)
