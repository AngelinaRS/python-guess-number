import random #This module will generate a random number

RANDOM_NUMBER = random.randint(1,20) #This variable saves the generated number from 1 to 20
print RANDOM_NUMBER

TURN = 1 #This counts the opportinities of the user
while TURN <=4: #The user only has 4 turns

	PROPOSAL_OF_THE_USER = int(input("Enter a number from 1 to 20")) #This variable saves the proposal of the user

	if PROPOSAL_OF_THE_USER == RANDOM_NUMBER: #This condition checks if the user guesses the number
		print "You win!"
		break #This breaks the loop

	elif PROPOSAL_OF_THE_USER > RANDOM_NUMBER: #This condition compares if the proposal of the user is higher than the generated number
		print "You guessed too high, please try again"
		TURN+=1 #This is for decrease the oportunities

	elif PROPOSAL_OF_THE_USER < RANDOM_NUMBER: #This condition compares if the proposal of the user is lower than the generated number
		print "You guessed too low, please try again"
		TURN+=1

else: #When the user loses the 4 opportunities
	print "Game Over"

	