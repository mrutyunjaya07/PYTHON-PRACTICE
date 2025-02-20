# WAP to display:
#  *
#  **
#  ***
#  ****

# Taking input from user
n = int(input("Enter a number: "))

# Loop to print the pattern
for i in range(n):
    for j in range(n):
        print("*", end=" ")  # Print stars in the same line
    
    print()  # Move to the next line after each row
