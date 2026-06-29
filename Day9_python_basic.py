Day 9 - List Functions and Methods
# Day 9 - List Functions and Methods

numbers = [30, 10, 20]

print("Original List:", numbers)

# Functions
print("Length:", len(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))

# Methods
numbers.append(40)
print("After append:", numbers)

numbers.extend([50, 60])
print("After extend:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

numbers.remove(20)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

numbers.sort()
print("After sort:", numbers)