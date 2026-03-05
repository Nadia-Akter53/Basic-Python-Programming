#Question:-17:-Find the index of the maximum value in a list.

numbers = [3,7,1,10,4]
max_val = numbers[0]
index = 0

for i in range(len(numbers)):
    if numbers[i] > max_val:
        max_val = numbers[i]
        index = i

print(index)
