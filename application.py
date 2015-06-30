import random #This module will generate a random number

New_Game = True
while New_Game == True: #This will run while the user want to play

	Random_Number = random.randint(1,20) #This variable saves the generated number from 1 to 20
	print Random_Number

	Turn = 1 #This counts the opportinities of the user
	while Turn <= 4: #The user only has 4 turns

		Proposal_of_the_user = int(input("Enter a number from 1 to 20")) #This variable saves the proposal of the user

		if Proposal_of_the_user == Random_Number: #This condition checks if the user guesses the number
			print "You win!"

			Random_Number = random.randint(1,20) #This generate other random number

			Answer_Winner = True
			while Answer_Winner == True: #when the user wins the game asks if want to play again
				Answer_of_the_user = raw_input("Do you want to play again? yes or no")
				Answer_of_the_user = Answer_of_the_user.lower()

				if Answer_of_the_user == "yes":
					Answer_Winner = False #if the answer of the user is "yes" no longer will ask
					New_Game = True #This will run the game again
				elif Answer_of_the_user == "no":
					Answer_Winner = False
					New_Game = False
					Turn = 5 #This will stop the game
				else:
					print "Only can write yes or no"
					Answer_Winner = True #The game only can accept "yes" or "no"

		elif Proposal_of_the_user > Random_Number: #This condition compares if the proposal of the user is higher than the generated number
			print "You guessed too high, please try again"
			Turn+=1 #This is for decrease the oportunities

		elif Proposal_of_the_user < Random_Number: #This condition compares if the proposal of the user is lower than the generated number
			print "You guessed too low, please try again"
			Turn+=1

	else: #When the user loses the 4 opportunities
		if New_Game == False:
			break
		else:
			print "Game Over"
			print "The number was: %d" % Random_Number
		Answer_Loser = True
		while Answer_Loser == True:
			Answer_of_the_user = raw_input("Do you want to play again? yes or no")
			Answer_of_the_user = Answer_of_the_user.lower()

			if Answer_of_the_user == "yes":
				Answer_Loser = False 
				New_Game = True

			elif Answer_of_the_user == "no":
				Answer_Loser = False
				New_Game = False
			else:
				print "Only can write yes or no"
				Answer_Loser = True
