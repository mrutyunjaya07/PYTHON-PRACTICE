from sys import argv

print("The Number of command line arguments :",len(argv))
print("The list of command line arguments :",argv)

print("Command line arguments one by on :")
for x in argv:
    print(x)