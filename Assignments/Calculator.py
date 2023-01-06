# radical function

num1 = int(input("Enter a number: "))
print("Type one of the functions: +  -  **")
function = input("Enter a function: ") # use list
num2 = int(input("Enter another number: "))



def add():
    added_num = num1 + num2
    return added_num

def sub():
    subtracted_num = num1 - num2
    return subtracted_num

def power():
    power_num = num1 ** num2
    return power_num


def choice():
    if function == "+":
        
