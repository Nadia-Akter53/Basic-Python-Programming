#Question:-18:-Normalize the values in a list between 0 and 1.

numbers = [2,5,10,3,8]
min_val = min(numbers)
max_val = max(numbers)
normalized = []

for x in numbers:
    normalized.append((x - min_val) / (max_val - min_val))

print(normalized)
