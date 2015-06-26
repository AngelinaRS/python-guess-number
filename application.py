import random #This module will generate a random number

RANDOM_NUMBER = random.randint(1,20) #This variable saves the number generated from 1 to 20
print RANDOM_NUMBER

PROPOSAL_OF_THE_USER = int(input("Enter a number from 1 to 20")) #This variable saves the proposal of the user

if PROPOSAL_OF_THE_USER > RANDOM_NUMBER: #This condition compares if the proposal of the user is higher than the number generated
	print "You guessed to high, please try again"