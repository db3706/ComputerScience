user_input = int(input("Enter a positive integer: "))

for num in range(1, user_input + 1):              # Sets the range from 1 to the user input
    if user_input % num == 0:                     # If the remainder of dividing the user input and the num variable is 0
        print(num,"is a factor of",user_input)    # Then print