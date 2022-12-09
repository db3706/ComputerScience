side1 = int(input("Enter a positive number: "))
side2 = int(input("Enter a second positive number: "))
side3 = int(input("Enter a third positive number: "))

def valid_triangle():
    if side1 == side2 and side2 == side3:
        return True
    elif side1 + side2 > side3 and side3 + side2 > side1 and side3 + side1 > side2:
        return True
    else:
        return False


if valid_triangle() == True:
    print("The numbers",side1,side2,side3,"form a valid triangle")
else:
    print("The numbers",side1,side2,side3,"do not form a valid triangle")