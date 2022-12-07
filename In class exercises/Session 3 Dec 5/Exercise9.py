

# Magic date check

year = 22
day = int(input("Enter what day it is today: "))
month = int(input("Enter what month it is today: "))


def magic_date():
    if day * month == year:
        print("Today is a magic date!")
    else:
        print("Sorry! Today isn't a magic date!")

magic_date()



