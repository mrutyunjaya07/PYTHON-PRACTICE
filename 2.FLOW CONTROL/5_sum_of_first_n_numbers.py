# To display the sum of fisrt n numbers

#taking input
n=int(input("Enter Number: "))

# initializing sum as 0
sum=0
i=1

while i<=n :
    sum= sum+i
    i+=1

print("The sum of the first ",n," number is : ",sum)