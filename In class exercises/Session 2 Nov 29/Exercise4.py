# User input 
user_input = int(input("Enter a whole number: "))

# initial variables
i = 1
factorial = 1

while i <= user_input:        # while i is less than the user input
    factorial = factorial * i # multiply the factorial by i
    i = i + 1                 # then add 1 to i and repeat until i is greater than user input

print("The factorial of",user_input,"is",factorial)