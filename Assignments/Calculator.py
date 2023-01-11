# radical function




def add():
    added_num = num1 + num2
    return added_num

def sub():
    subtracted_num = num1 - num2
    return subtracted_num

def power():
    power_num = num1 ** num2
    return power_num

def multi():
    multiplied_num = num1 * num2
    return multiplied_num


print("Type one of the functions: +  -  **  sq")
function = input("Enter a function: ") 
if function == "+":
    print("_ + _")
    num1 = int(input("Enter a number: "))
    print(num1,"+ _")
    num2 = int(input("Enter another number: "))
    print(num1,"+",num2,"=",add())
elif function == "-":
    print("_ - _")
    num1 = int(input("Enter a number: "))
    print(num1,"- _")
    num2 = int(input("Enter another number: "))
    print(num1,"-",num2,"=",sub())
