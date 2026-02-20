#Question:-06:Convert a list of integers to a list of booleans where all non-zero values become True.


terms = int(input("Enter the Range of values: "))
numbers = []

for n in range(terms):
    numbers.append(bool(n))

print(numbers)
