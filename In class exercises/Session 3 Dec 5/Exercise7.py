# f(2) = 2.95(x - 1) + 10.95
# f(x) = 2.95(x - 1) + 10.95
# f(1) = 0 + 10.95

# x - 1 because the first order is not included

def shipping_cost(items):
    num = 2.95 * (items - 1) + 10.95
    return num

user_input = int(input("Enter a positive number of items: "))
while user_input < 0:
    user_input = (int(input("Reenter a POSITIVE number: ")))
    print(user_input)
else:
    user_input = round(shipping_cost(user_input),2)
    print("Total shipping charge is: $",user_input)