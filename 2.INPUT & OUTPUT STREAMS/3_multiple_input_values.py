# Read 3 float numbers from the keyboard with ',' separator and print their sum

# Taking input and splitting based on ','
numbers = input("Enter three float numbers separated by commas: ").split(",")

# Unpacking values correctly
a, b, c = (float(x) for x in numbers)

# Print the sum
print("Sum is:", a + b + c)
