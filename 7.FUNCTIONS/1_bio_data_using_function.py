# display biodata using function

def bioData() :
    name=input("Your name : ")
    rollNo=input("your roll no : ")
    contactNo =input("your contact no : ")
    address=input("Your address : ")
   
    #empty lines for space
    print()
    print()

    print("your name is ",name)
    print("your roll number is ",rollNo)
    print("your contact number is ",contactNo)
    print("your address is ",address)

# function calling
bioData()