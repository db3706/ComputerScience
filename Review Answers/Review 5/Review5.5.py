# 1. Write a script that asks the user to input a number and then dis-
#    plays that number rounded to two decimal places. When run, your program should look like this:
#       Enter a number: 5.432
#       5.432 rounded to 2 decimal places is 5.43

user_input = input("Enter a number: ")
num = float(user_input)
print(str(user_input) + " rounded to 2 decimal places is " + str(round(num, 2)))

# 2. Write a script that asks the user to input a number and then dis-
#    plays the absolute value of that number. When run, your program should look like this:
#       Enter a number: -10
#       The absolute value of -10 is 10.0

user_input = float(input("Enter a number: "))
print("The absolute value of " + str(user_input) + " is " + str(abs(user_input)))

# 3. Write a script that asks the user to input two numbers by using the
#    input() function twice, then display whether or not the difference
#    between those two number is an integer. When run, your program should look like this:
#       Enter a number: 1.5
#       Enter another number: .5
#       The difference between 1.5 and .5 is an integer? True!
#   If the user inputs two numbers whose difference is not integral, the output should look like this:
#       Enter a number: 1.5
#       Enter another number: 1.0
#       The difference between 1.5 and 1.0 is an integer? False!

user_input1 = float(input("Enter a number: "))
user_input2 = float(input("Enter another number: "))
difference = float(user_input1 - user_input2) 

print("The difference between " + str(user_input1) + " and " + str(user_input2) + " is an integer?") 
print(difference.is_integer())
