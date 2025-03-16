import sys


def sum_geometric(initial,ratio,n):
# Write a function called 'sum_geometric'.
# Purpose: Given an initial value, an incremement, and a number, n, what is the sum of a
#	geometric series up to n elements?
# Input: an initial number, 'initial', an geometric ratio value, 'ratio', and a number, 'n', representing 
#	the number of elements in the series.
# Output: the sum of the geometric series of length 'n', initial value, 'initial', and geometric ratio
#	value, 'ratio'.

	# Type your code here...



if __name__ == '__main__':
# HERE is the main block of code! The computer will go here first.

	# Set the values of initial, ratio, and n to test your code.
	initial = 1
	ratio = 2
	n = 5

	# Do not touch these lines of code!
	x = sum_geometric(initial,ratio,n)
	print('\n' + str(x) + '\n')