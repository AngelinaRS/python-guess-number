import random #This module will generate a random number

RANDOM_NUMBER = random.randint(1,20) #This variable saves the generated number from 1 to 20
print RANDOM_NUMBER

PROPOSAL_OF_THE_USER = int(input("Enter a number from 1 to 20")) #This variable saves the proposal of the user

if PROPOSAL_OF_THE_USER > RANDOM_NUMBER: #This condition compares if the proposal of the user is higher than the generated number
	print "You guessed too high, please try again"

elif PROPOSAL_OF_THE_USER < RANDOM_NUMBER: #This condition compares if the proposal of the user is lower than the generated number
	print "You guessed too low, please try again"

elif PROPOSAL_OF_THE_USER == RANDOM_NUMBER: #This condition checks if the user guesses the number
	print "You win!"