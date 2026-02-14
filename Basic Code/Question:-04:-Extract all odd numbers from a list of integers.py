#Question:-04:-Extract all odd numbers from a list of integers.

terms = int(input("Enter the Range of values: "))
numbers = []

for n in range(terms):
  if n % 2 != 0:
    numbers.append(n)


print(numbers)
