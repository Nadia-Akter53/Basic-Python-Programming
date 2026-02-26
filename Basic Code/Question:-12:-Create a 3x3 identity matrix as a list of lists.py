#Question:-12:-Create a 3x3 identity matrix as a list of lists.

matrix = []

for i in range(3):
    row = []
    for j in range(3):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

print(matrix)
