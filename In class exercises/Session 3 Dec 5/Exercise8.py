num = int(input("Enter an integer: "))

def prime_check(num): 
    # establishes the range from 2 to one below the user input
    for divisor in range(2, num): 
        # If ANY remainder returns as 0
        if (num % divisor) == 0:  
            # return false, which means that it's NOT a prime number
            return False           
    # If not, return true, which means that it IS a prime number        
    return True        


# Check if the function returned as true or false
if prime_check(num) == True:
    print(num,"is a prime number.")
else:
    print(num,"is not a prime number.")


