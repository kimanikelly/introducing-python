# Any sequence of digits represents a literal integer
literal_integer = 5

# A plain zero is a valid literal integer
zero_integer = 0

# Cant have an initial zero followed a digit between 1 and 9
# Example
# error = 09

# A sequence of integers specifies a positive integer
positive_num_one = 123
print(positive_num_one)


# If you put a + sign before the digits the number stays the same
positive_num_two = +123
print(positive_num_two)

# To specify a negative number insert a - sign before the digits
negative_num = -123
print(negative_num)

# Commas are not allowed in integers. Commas in integers will return a tuple type
tuple_example = 1, 000, 000
print("tuple type:", type(tuple_example))

# Underscores can be used a digit separator
underscore_example = 1_000_000
print("int type:", type(underscore_example))
