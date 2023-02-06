# Imports
import random
import time
def insertion_sort(list_a):
    # indexing length is from first value to all following values
    indexing_length = range(1, len(list_a))
    # for every value in indexing_length
    for i in indexing_length:
        value_to_sort = list_a[i]
        # if the value to the left is greater than the value to the right
        while list_a[i-1] > value_to_sort and i>0:
        # then swap the position of those two values
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            # then subtract 1 to incrementally progress through the list
            i = i -1
    return list_a


# Set data to a list of 10,000 random values
# The actual values range from 1 to 100,000
data = list(random.sample(range(1, 100000), 10000))
# Start the timer
start = time.time()
print('Sorted Array in Ascending Order:')
print(insertion_sort(data))
# End the timer
end = time.time()
# Print the time required to finish sorting in seconds, rounded to two decimal places
print("Time required: ", round((end - start), 2),"seconds")

# Credits: https://youtu.be/byHi41L9vTM