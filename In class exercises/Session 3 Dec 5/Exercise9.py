# Magic date check

year = 22
day = int(input("Enter what day it is today (As a number): "))
month = int(input("Enter what month it is today (As a number): "))


def magic_date():
    # If the day multiplied by the month is equal to the 2 digit year (22)
    if day * month == year:     
        # then print that today is a magic date
        print("Today is a magic date!") 
    else:
        # if not, print otherwise
        print("Sorry! Today isn't a magic date!") 

magic_date()



