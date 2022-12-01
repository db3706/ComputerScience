user_input = int(input("Enter an integer: "))

for count in range(1, user_input + 1):   # 1 is added to the user input since the range only includes numbers lower than the value
    cube = count ** 3                    #Exponent operator
    print("Current Number is:", count, "and the cube is", cube)


