# Imports
import time
import random

# Bubble sort algorithm
def bubble(list_a):
    indexing_length = len(list_a) - 1 
    sorted = False 
    # As long as sorted = False, execute the loop below
    while not sorted: 
        sorted = True  
        for i in range(0, indexing_length): 
            # if the value to the left is greater than the value to the right
            if list_a[i] > list_a[i+1]:
            # then set sorted to False
                sorted = False 
            # and swap the positions of the two values
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] 
    return list_a 


# Set data to a list of 10,000 random values
# The actual values range from 1 to 100,000
data = list(random.sample(range(1, 100000), 10000))
# Start the timer
start = time.time()
print('Sorted Array in Ascending Order:')
print(bubble(data))
# End the timer
end = time.time()
# Print the time required to finish sorting in seconds, rounded to two decimal places
print("Time required: ", round((end - start), 2),"seconds")

# Credits: https://youtu.be/g_xesqdQqvA