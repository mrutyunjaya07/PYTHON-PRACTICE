# WAP to read employee data from the keyboard and print that data !!


#taking input data
eno=int(input("Enter Employee No: "))
ename=input("Enter Employee Name: ")
esal=float(input("Enter Employee Salary: "))
eadd=input("Enter Employee Address: ")
emarried=bool(input("Enter Employee Married ?[True | False]: "))

#printing data
print("Confirm Information")
print("Employee No :",eno)
print("Employee Name :",ename)
print("Employee Salary :",esal)
print("Employee Address :",eadd)
print("Employee Married? :",emarried)