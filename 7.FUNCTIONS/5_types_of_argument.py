# Types of argument :
    # positional
    # keyword
    # default
    # variable length



# positional arguments :

# number of arguments should be same
def sub(a,b):
    print(a-b)

sub(100,200) #-100
sub(200,100) # 100


# keyword arguments :

#here order is not important but number of arguments should be same

def wish(name,msg):
    print("Hello",name,".",msg)

wish(name="MJ",msg="good mrng....")
wish(msg="good mrng....",name="MJ")


# while using both     positional arg --> keyword arg



# default arguments :

# default value to positional arguments

def wish(name="MJ") :
    print("Hay",name,"Good morning !!")


wish() # with no arguments the default value will be printed
wish("Hari")


