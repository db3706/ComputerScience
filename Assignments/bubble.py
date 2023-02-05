# imports
import time

# helper methods
def swap(A, i, j):
	A[i], A[j] = A[j], A[i]


# algorithms
def bubblesort(A):
	swapped = True
	
	for i in range(len(A) - 1):
		if not swapped:
			return
		swapped = False
		
		for j in range(len(A) - 1 - i):
			if A[j] > A[j + 1]:
				swap(A, j, j + 1)
				swapped = True
			yield A

