# radical function

num1 = int(input("Enter a number: "))
print("Type one of the functions: +  -  **")
function = input("Enter a function: ") # use list
num2 = int(input("Enter another number: "))



def add(added_num):
    num1 + num2 == added_num
    return added_num

def sub(subtracted_num):
    num1 - num2 == subtracted_num
    return subtracted_num

def power(power_num):
    num1 ** num2 == power_num
    return power_num

def fchoice():
    if function == "+":
        return add()
print(fchoice())

