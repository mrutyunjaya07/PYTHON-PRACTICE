# WAP to display:
#  *
#  **
#  ***
#  ****

# Taking input from user
n = int(input("Enter a number: "))

# Loop to print the pattern
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")  # Print stars in the same line
    print()  # Move to the next line after each row


    
