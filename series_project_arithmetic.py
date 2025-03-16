import sys
import random



def sum_arithmetic(initial,increment,n):
# The name of the function is 'sum_arithmetic'.
# Purpose: Given an initial value, an incremement, and a number, n, what is the sum of an
#	arithmetic series up to n elements?
# Input: an initial number, 'initial', an increment value, 'increment', and a number, 'n', representing 
#	the number of elements in the series.
# Output: the sum of the arithmetic series of length n, initial value, initial, and increment
#	value, increment.

	sum = initial	# Creates a variable, sum, and sets its value as initial

	# Continue your code below...


	return sum		# When the for-loop is over, the function spits out the value of 'sum'.
							

if __name__ == '__main__':
# HERE is the main block of code! The computer will go here first.

	# Set the values of initial, increment, and n to test your code.
	initial = 1
	increment = 2
	n = 5

	# Do not touch these lines of code!
	x = sum_arithmetic(initial,increment,n)
	print('\n' + str(x) + '\n')