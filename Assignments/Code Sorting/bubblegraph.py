# Imports
import random
from matplotlib import pyplot as plt, animation

# Swap function
def swap(A, i, j):
	# Swaps the positions of two numbers in the array
	A[i], A[j] = A[j], A[i]


# Bubble sort algorithm
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


# Matplotlib function
def visualize():
	# Set a list of random values ranging from 1 to 100
	N = random.sample(range(1, 101), 100)
	A = list(N)
	random.shuffle(A)
	
	# Creates a generator object containing all
	# the states of the array while performing
	# sorting algorithm
	generator = bubblesort(A)
	
	# Creates a figure and subsequent subplots
	fig, ax = plt.subplots()
	ax.set_title("Bubble Sort O(n\N{SUPERSCRIPT TWO})")
	bar_sub = ax.bar(range(len(A)), A, align="edge")

	# Labeling the x and y axis
	plt.xlabel("# of values")
	plt.ylabel("Value")

	
	# Sets the maximum limit to 100 for the x-axis
	ax.set_xlim(0, 100)
	text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
	iteration = [0]
	
	# Function to update each frame in plot
	def update(A, rects, iteration):
		for rect, val in zip(rects, A):
			rect.set_height(val)
		iteration[0] += 1
		text.set_text(f"# of operations: {iteration[0]}")
	

	# Creating animation object for rendering the iteration
	anim = animation.FuncAnimation(
		fig,
		func=update,
		fargs=(bar_sub, iteration),
		frames=generator,
		# Repeat set to False so the operation count stops once done sorting
		repeat=False,
		blit=False,
		interval=15,
		save_count=90000,
	)
	# For showing the animation on screen
	plt.show()

# Start the matplotlib graph
visualize()



