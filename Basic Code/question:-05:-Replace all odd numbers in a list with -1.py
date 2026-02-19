#question:-05:-Replace all odd numbers in a list with -1..

terms = int(input("Enter the Range of values: "))
numbers = []

for n in range(terms):
  if n % 2 != 0:
    numbers.append(-1)
  else:
    numbers.append(n)


print(numbers)
