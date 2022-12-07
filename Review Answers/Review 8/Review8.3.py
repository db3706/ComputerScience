user_input = input("Enter a word: ")

# Checks if the user input is less than or greater than 5 and prints accordingly
if len(user_input) < 5:
    print(user_input,"is less than 5 characters.")

elif len(user_input) > 5:
    print(user_input,"is more than 5 characters.")

 # If the word doesn't meet any of the above conditions, then it must be equal to 5
else:
    print(user_input,"is equal to 5 characters.")
