#Question:-02:-Convert a list of integers to a list of strings.

terms = int(input("Enter the Range of values: "))
numbers = []

for n in range(terms):
    numbers.append(str(n))

print(numbers, end="")
