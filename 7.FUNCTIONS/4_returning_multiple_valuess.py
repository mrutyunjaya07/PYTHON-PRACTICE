# function returning multiple values 

# defining function
def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div     # returning multiple values

t=calc(100,50)    # as a tuple

print(t)
print(type(t))
print("The Results are:")

# accessing values from tuple using loop
for i in t:
    print(i)                 


    