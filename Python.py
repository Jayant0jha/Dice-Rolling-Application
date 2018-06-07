import random

def dice():

	loop = "y"

	while loop == "y":

		print ("Rolling the dice...")
		print ("The value is..")
		print random.randint(1,6)
		loop = raw_input("Roll the dice again('y' or 'n')? ")

dice()
