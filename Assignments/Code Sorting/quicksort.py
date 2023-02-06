# Imports
import time
import random

# Quicksort algorithm
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        # pop() removes a value from a specified locaiton and returns it
        pivot = sequence.pop()

    # values greater than pivot
    items_greater = []
    # values less than pivot
    items_lower = []

    for item in sequence:
        # if the value is greater than pivot,
        # append the value to the items_greater list
        if item > pivot:
            items_greater.append(item)
        # if the value is less than pivot,
        # append the value to the items_lower list
        else:
            items_lower.append(item)
    # apply the algorithm again to items_lower, the pivot in the center, and items_greater
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)




# Set data to a list of 10,000 random values
# The actual values range from 1 to 100,000
data = list(random.sample(range(1, 100000), 10000))
# Start the timer
start = time.time()
print('Sorted Array in Ascending Order:')
print(quick_sort(data))
# End the timer
end = time.time()
# Print the time required to finish sorting in seconds, rounded to two decimal places
print("Time required: ", round((end - start), 2),"seconds")

# Credits: https://youtu.be/kFeXwkgnQ9U