# largest between three numbers

#taking input
n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter third Number:"))


#comparing using conditionals
if n1>n2 and n1>n3:
    print("Biggest Number is:",n1)
elif n2>n3:
    print("Biggest Number is:",n2)
else:
    print("Biggest Number is:",n3 )