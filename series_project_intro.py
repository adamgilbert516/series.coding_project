import sys
import random

#The line above is responsible for making this entire file "executable"...
# in other words, this file would not run without it because of complicated
# computer stuff.

def print_message(str):
# This function is called 'print_message'. The parameter str is a string.
# Purpose: To print the message passed into the function, unless the message
#	is 'Math is boring!'. Then the message must be changed!
# Input: a string (some secret message)
# Output: none

	a = str 	# Set a variable, a, equal to the parameter str
	
	## WRITE YOUR ANSWER TO QUESTION 6 BELOW:
	



	print(a) 	# Print the final value of a.


if __name__=="__main__":
# This is the main block of code, from which the computer will execute! In other words,
#	when you run a python program in terminal, the computer runs the lines below 
#	'if __name__ == "__main__":' first.

	
	# Change the value of 'i_am_a_variable' to test your code.

	i_am_a_variable = 'Math is okay!' 	# Notice the indent is exactly 4 spaces in.

	print_message(i_am_a_variable) 		# Here is where the function defined above is called, 
										# where the variable is passed as a parameter. Notice that this 
										# line is vertically aligned with the line above it.
										# VARIABLES CAN BE PASSED INTO FUNCTIONS AS PARAMETERS. THIS 
										# VARIABLE HAS AN ACTUAL VALUE THAT THEN RUNS THROUGH 
										# THE FUNCTION print_message.


