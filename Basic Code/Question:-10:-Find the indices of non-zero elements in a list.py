#Question:-10:-Find the indices of non-zero elements in a list.

numbers = [1, 2, 0, 0, 4, 0]
indices = []

for i in range(len(numbers)):
    if numbers[i] != 0:
        indices.append(i)

print(indices)
