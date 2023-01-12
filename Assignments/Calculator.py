from fractions import Fraction

# This function gives the option of continuing or shutdowning the calculator after a successful calculation
def finalchoice():
    print(" ")
    print("Would you like to continue using the calculator?")
    print("Type 1 for Yes | 2 for No")
    num1 = float(input("Enter 1 or 2 here: "))
    if num1 == 1:
        op_choice()
    elif num1 == 2:
        exit()
    else:
        print("1 or 2 was not inputted. Please choose again.")
        finalchoice()

# Integer check
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

# Fraction check for radical() function. Resources outside course material was used for this.
def isfloat(num):
    try:
        float(Fraction(num))
        return True
    except ValueError:
        return False

# All the functions that contain the calculations below:
def add():
    print("_ + _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == True:
        print(num1,"+ _")
    else:
        print("Invalid input value. Please choose again.")
        add()
    num2 = input("Enter another number: ")
    if is_integer(num2) == True:
        print(num1,"+",num2,"=",float(num1) + float(num2))
        finalchoice()
    else:
        print("Invalid input value. Please choose again")
        add()

def sub():
    print("_ - _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == True:
        print(num1,"- _")
    else:
        print("Invalid input value. Please choose again.")
        sub()
    num2 = input("Enter another number: ")
    if is_integer(num2) == True:
        print(num1,"-",num2,"=",float(num1) - float(num2))
        finalchoice()
    else:
        print("Invalid input value. Please choose again")
        sub()

def multiply():
    print("_ * _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == True:
        print(num1,"* _")
    else:
        print("Invalid input value. Please choose again.")
        multiply()
    num2 = input("Enter another number: ")
    if is_integer(num2) == True:
        print(num1,"*",num2,"=",float(num1) * float(num2))
        finalchoice()
    else:
        print("Invalid input value. Please choose again.")
        multiply()

def divide():
    print("_ / _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == True:
        print(num1,"/ _")
    else:
        print("Invalid input value. Please choose again.")
        divide()
    num2 = input("Enter another number: ")
    if is_integer(num2) == True and float(num2) > 0:
        print(num1,"/",num2,"=",float(num1) / float(num2))
        finalchoice()
    elif float(num2) == 0:
        print("Bad input, cannot divide by 0. Please choose again")
        divide()
    else:
        print("Invalid input value. Please choose again.")
        divide()

def squareroot():
    print("√ _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == False:
        print("Invalid input value. Please choose again. ")
        squareroot()
    elif float(num1) >= 0:
       print("√",num1,"=",float(num1) ** 0.5)
       finalchoice()
    else:
       print("Cannot squareroot negative.")
       squareroot()

def power():
    print("_ ** _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == True:
        print(num1,"** _")
    else:
        print("Invalid input value. Please choose again.")
        power()
    num2 = input("Enter another number: ")
    if is_integer(num2) == True:
        print(num1,"**",num2,"=",float(num1) ** float(num2))
        finalchoice()
    else:
        print("Invalid input value. Please choose again")
        power()

def radical():
    print("_ ** _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == True:
        print(num1,"** _")
    else:
        print("Invalid input value. Please choose again.")
        radical()
    num2 = input("Enter a fraction in the form of x/y: ")
    if isfloat(num2) == True:
        print(num1,"**",num2,"=",float(num1) ** float(Fraction(num2)))
        finalchoice()
    else:
        print("Invalid input value. Please choose again")
        radical()

def modulus():
    print("_ % _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == True:
        print(num1,"% _")
    else:
        print("Invalid input value. Please choose again.")
        modulus()
    num2 = input("Enter another number: ")
    if is_integer(num2) == True:
        print(num1,"%",num2,"=",float(num1) % float(num2))
        finalchoice()
    else:
        print("Invalid input value. Please choose again.")
        modulus()



   
# prints the list of choices of operators
list = ['1. Add','2. Subtract','3. Multiply','4. Divide',"5. Square Root","6. Power","7. Radical","8. Modulus"]
print("Note: Fractions can only be used with the Radical operator.")
for number in list:
    print(number)

# function that contains the user's operator choice
def op_choice():
    operator = input("Type a number corresponding to an operator from the list: ")
    if float(operator) < 1 or float(operator) > 8:
        print("Invalid input value. Please choose a number from the list.")
    elif is_integer(operator) == False:
        print("Invalid input value. Please choose a number from the list.")
    else:
# Depending on the user's choice, a certain operator will be called
        if operator == "1":
            add()
    
        elif operator == "2":
            sub()
    
        elif operator == "3":
            multiply()

        elif operator == "4":
            divide()

        elif operator == "5":
            squareroot()

        elif operator == "6":
            power()

        elif operator == "7":
            radical()
        elif operator == "8":
            modulus()

# Starts the calculator
op_choice()
