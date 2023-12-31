# For Loop

numbers = [1, 2, 3, 4, 5, 6]
doubled_numbers = []
for num in numbers:
    doubled_numbers.append(num * 2)
print(doubled_numbers)

# List Comprehension

numbers = [1, 2, 3, 4, 5, 6]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

# String as List

name = 'Levi'
letters_list = [letter for letter in name]
print(letters_list)

# Range as List

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

# Conditional List Comprehension

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
