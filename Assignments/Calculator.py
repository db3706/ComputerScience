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

# All the functions that contain the calculations are below:
def add():
    print("_ + _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == True:
        print(num1,"+ _")
    else:
        print("--Invalid input value. Please choose an integer.")
        add()
    num2 = input("Enter another number: ")
    if is_integer(num2) == True:
        print(num1,"+",num2,"=",int(num1) + int(num2))
        finalchoice()
    else:
        print("--Invalid input value. Please choose an integer.")
        add()

def sub():
    print("_ - _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == True:
        print(num1,"- _")
    else:
        print("--Invalid input value. Please choose an integer.")
        sub()
    num2 = input("Enter another number: ")
    if is_integer(num2) == True:
        print(num1,"-",num2,"=",int(num1) - int(num2))
        finalchoice()
    else:
        print("--Invalid input value. Please choose an integer.")
        sub()

def multiply():
    print("_ * _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == True:
        print(num1,"* _")
    else:
        print("--Invalid input value. Please choose an integer.")
        multiply()
    num2 = input("Enter another number: ")
    if is_integer(num2) == True:
        print(num1,"*",num2,"=",int(num1) * int(num2))
        finalchoice()
    else:
        print("--Invalid input value. Please choose an integer.")
        multiply()

def divide():
    print("_ / _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == True:
        print(num1,"/ _")
    else:
        print("--Invalid input value. Please choose an integer.")
        divide()
    num2 = input("Enter another number: ")
    if num2 == 0:
        print("--Bad input, cannot divide by 0. Please choose an integer")
        divide()     
    elif is_integer(num2) == True:
        print(num1,"/",num2,"=",int(num1) / int(num2))
        finalchoice()
    else:
        print("--Invalid input value. Please choose an integer.")
        divide()

def squareroot():
    print("√ _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == False:
        print("--Invalid input value. Please choose a positive integer. ")
        squareroot()
    elif float(num1) >= 0:
       print("√",num1,"=",float(num1) ** 0.5)
       finalchoice()
    else:
       print("--Cannot squareroot negative.")
       squareroot()

def power():
    print("_ ** _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == True:
        print(num1,"** _")
    else:
        print("--Invalid input value. Please choose an integer.")
        power()
    num2 = input("Enter another number: ")
    if is_integer(num2) == True:
        print(num1,"**",num2,"=",int(num1) ** int(num2))
        finalchoice()
    else:
        print("--Invalid input value. Please choose an integer.")
        power()

def radical():
    print("_ ** _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == True:
        print(num1,"** _")
    else:
        print("--Invalid input value. Please choose an integer.")
        radical()
    num2 = input("Enter a fraction in the form of x/y: ")
    if isfloat(num2) == True and is_integer(num2) == False:
        print(num1,"**",num2,"=",float(num1) ** float(Fraction(num2)))
        finalchoice()
    else:
        print("--Invalid second input value. Fraction is expected.")
        radical()

def modulus():
    print("_ % _")
    num1 = input("Enter a number: ")
    if is_integer(num1) == True:
        print(num1,"% _")
    else:
        print("--Invalid input value. Please choose an integer.")
        modulus()
    num2 = input("Enter another number: ")
    if is_integer(num2) == True:
        print(num1,"%",num2,"=",int(num1) % int(num2))
        finalchoice()
    else:
        print("--Invalid input value. Please choose an integer.")
        modulus()


# Prints the list of choices of operators
list = ['1. Add','2. Subtract','3. Multiply','4. Divide',"5. Square Root","6. Power","7. Radical","8. Modulus"]
print("Note: Fractions can only be used with the Radical operator.")
for number in list:
    print(number)

# Function that contains the user's operator choice
def op_choice():
    operator = input("Type a number corresponding to an operator from the list: ")
    if is_integer(operator) == False:
        print("--Invalid input value. Please choose a valid DIGIT to perform.")
        op_choice()
    elif float(operator) < 1 or float(operator) > 8:
        print("--Invalid input value. Please choose a number from 1 to 7")
        op_choice()
    else:

# Depending on the user's operator choice, a certain function will be called
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
