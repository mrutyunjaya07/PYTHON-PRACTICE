# when a function calls itself for solving a problem is know as recursive function


#function definition
def add(number):
    sum=0     # initialize sum as o

    #small case
    if number ==0:
        return 0
    else:
        #recursive call
        sum=number+ add(number-1)

        # return statement
        return sum
    
# taking input from user
num=int(input("Enter the number :"))

# function call
sumfinal=add(num)
# printing value
print(f"Sum of first {num} number is :",sumfinal)




