#Question:-01: Create a list with values ranging from 0 to 9.

terms = int(input("Enter the Range of values: "))
numbers = []

for n in range(terms):
    numbers.append(n)

print(numbers, end="")
