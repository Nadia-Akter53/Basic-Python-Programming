#Question:-16:- Create a 5x5 list of lists with row values ranging from 0 to 4.

matrix = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(j)
    matrix.append(row)

print(matrix)
