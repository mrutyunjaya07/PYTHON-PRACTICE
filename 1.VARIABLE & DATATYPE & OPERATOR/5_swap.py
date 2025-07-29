# swap two numbers given
a=2
b=4
temp_var=a
a=b
b=temp_var

print("a = "+str(a)+" b = "+ str(b))

#without using temp_var
a=3
b=5
a = a + b
b = a - b
a = a - b

print(a, b)