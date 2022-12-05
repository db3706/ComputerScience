

def fahr_to_celsius(temp): #function signature
    #Beginning of my function body

    return (temp - 32) * (5/9)

# Combined print and function call statement
user_input = int(input("Enter a temperature in fahrenheit to convert to celsius: "))
print(round(fahr_to_celsius(user_input),2))

def celsius_to_fahr(temp):
    f_temp = temp * (9/5) + 32
    return f_temp

# Combined print and fnction call statement
user_input2 = int(input("Enter a temperature in celsius to convert to fahrenheit: "))
print(round(celsius_to_fahr(user_input2),2))