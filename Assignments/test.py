import random
# swap function
def swap(A, i, j):
	A[i], A[j] = A[j], A[i]


# bubble sort algorithm
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
			return A

N = random.sample(range(1, 10), 9)
A = list(N)
random.shuffle(A)

print(bubblesort(A))
