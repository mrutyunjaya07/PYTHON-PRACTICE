# Function to find factorial of a number using recursion



def factorial(num):
    # Factorial is not defined for negative numbers
    if num < 0:
        return "Factorial is not defined for negative numbers!"
    
    # Base case
    if num == 0 or num == 1:
        return 1
    
    # Recursive case
    return num * factorial(num - 1)


# Taking input
number = int(input("Enter the number: "))

# Function call
factorial_value = factorial(number)

# Output result
print("The factorial value of the given number is:", factorial_value)
