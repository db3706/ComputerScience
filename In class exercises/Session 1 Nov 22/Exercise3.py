# User input
integer_input = int(input("Enter an integer: "))

# If the integer's remainder is 0, then it's even
if (integer_input % 2) == 0: 
    print("The integer " + str(integer_input) + " is even")

# If the integer's remainder is not 0, then it's odd
else: 
    print("The integer " + str(integer_input) + " is odd")