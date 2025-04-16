# uses:

# we can pass lambda function in another functions arguments
# with filter(), map(), reduce() functions as they excepts function as arguments


# filter(function, sequence)
      # function should return True or False
      # gives the elemnts following the function

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



# map(function, sequence)
  # gives the new elemnts based on function

l1=[2,6,3,15,9]

l2=list(map(lambda n:2*n,l1))

print(l2)


# both list should be of same size
l3=[2,5,3,1]
l4=[1,0,5,8]

l5=list(map(lambda a,b:a*b,l3,l4))
print(l5)




# reduce( )
   #reduces sequence of elements into a single element by applying the specified function.
   # import functools module

from functools import *
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result)