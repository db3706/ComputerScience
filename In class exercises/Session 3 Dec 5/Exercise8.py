# Function
num = int(input("Enter an integer: "))

def prime_check(num):
     for divisor in range(2, num):
         if (num % divisor) == 0:
             return True
         else:
             return False
             break



if prime_check(num) == False:
    print("Prime")
else:
    print("Not Prime")


