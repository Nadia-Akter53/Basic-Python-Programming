#Question:-03:Multiply all elements in a list by 2.

terms = int(input("Enter the Range of values: "))
numbers = []

for n in range(terms):
    numbers.append(2*n)

print(numbers, end="")
