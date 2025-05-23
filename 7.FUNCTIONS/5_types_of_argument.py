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


# variable length arguments :

#we can give variable number of arguments

def sum(*num):    # creates a tuple named num
    total=0
    for i in num:
        total=total+i
    print("Sum is :",total)

sum()
sum(10,30)
sum(1,78,56)
sum(-12,90,0,789)

# for variable numbers of keyword arguments use --> **kwargs

# for simultenous use :   positional  --> *args --> keyword --> **kwargs
