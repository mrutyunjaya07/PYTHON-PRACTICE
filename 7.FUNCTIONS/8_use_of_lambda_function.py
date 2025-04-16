# uses:

# we can pass lambda function in another functions arguments
# with filter(), map(), reduce() functions as they excepts function as arguments


# without using lambda function
def isEven(num):
    if num%2==0:
        return True
    else:
        return False
    
l=[2,45,6,7,0,17,12]
print(type(filter(isEven,l)))

l1=list(filter(isEven,l))
print(l1)


# using lambda function

l=[87,67,54,4,13,9,28,3,54]
l1=list(filter(lambda n:n%2==0,l))
l2=list(filter(lambda n:n%2!=0,l))

print(l1,l2)


