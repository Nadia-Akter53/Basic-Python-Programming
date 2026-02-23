#Question:-09:-Calculate the sum of the diagonal elements of a 3x3 matrix (list of lists)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
sum_diag = 0

for i in range(3):
    sum_diag += matrix[i][i]

print(sum_diag)
