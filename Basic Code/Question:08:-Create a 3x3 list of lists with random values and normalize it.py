#Question:08:-Create a 3x3 list of lists with random values and normalize it.

import random

matrix = []
values = []

for i in range(3):
    row = []
    for j in range(3):
        num = random.randint(1, 10)
        row.append(num)
        values.append(num)
    matrix.append(row)

min_val = min(values)
max_val = max(values)

normalized = []
for row in matrix:
    n_row = []
    for x in row:
        n_row.append((x - min_val) / (max_val - min_val))
    normalized.append(n_row)

print(normalized)
