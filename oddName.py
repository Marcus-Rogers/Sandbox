"""Marcus Rogers"""

user_name = input("Please enter your name: ")
while user_name == "" or user_name == " ":
    user_name = input("Name cannot be blank. Please enter a valid name: ")

print(user_name[1::2])