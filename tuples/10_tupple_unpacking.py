# A tuple with three elements
my_tuple = (1, 2, 3)

# Tuple unpacking
a, b, c = my_tuple

# Now a is 1, b is 2, and c is 3
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3




# Tuple with more than three elements
my_tuple = (1, 2, 3, 4, 5)

# Unpacking with * operator
a, b, *rest = my_tuple

# Now a is 1, b is 2, and rest is [3, 4, 5]
print(a)    # Output: 1
print(b)    # Output: 2
print(rest) # Output: [3, 4, 5]
