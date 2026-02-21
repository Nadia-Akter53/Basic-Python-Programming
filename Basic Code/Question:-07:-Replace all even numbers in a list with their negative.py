#Question:-07:-Replace all even numbers in a list with their negative.

terms = int(input("Enter the Range of values: "))
numbers = []

for n in range(terms):
  if n % 2 == 0:
    numbers.append(-n)
  else:
    numbers.append(n)


print(numbers)
