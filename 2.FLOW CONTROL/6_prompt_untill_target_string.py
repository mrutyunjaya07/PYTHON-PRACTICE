#prompt user to enter name & pwd until mj & python


# Define empty strings
user_name = ""
pass_word = ""

# Keep asking until the correct credentials are entered
while user_name != "mj" or pass_word != "python":
    user_name = input("Enter correct username: ")
    pass_word = input("Enter correct password: ")

print("Thanks for confirmation.")
