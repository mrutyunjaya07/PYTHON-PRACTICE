# check a given number is odd or even

def oddEven(num) :

    if num%2==0 :
        print(f"{num} is even.")
    else :
        print(f"{num} is odd.")


number=int(input("Enter a number : "))
oddEven(number)