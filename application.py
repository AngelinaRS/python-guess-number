"""Guess Number"""
import random #This module will generate a random number

print "Welcome to game GUESS NUMBER"
print "You will have to guess a number in the range from 1 to 20"

NEW_GAME = True
while NEW_GAME == True: #This will run while the user want to play

#This variable saves the generated number from 1 to 20
    RANDOM_NUMBER = random.randint(1, 20)
    print RANDOM_NUMBER

    TURN = 1
    #This counts the opportinities of the user
    while TURN <= 4: #The user only has 4 TURNs
        try: #probabilities of errors of the user
            #This variable saves the proposal of the user
            PROPOSAL_OF_THE_USER = int(raw_input("Enter a number from 1 to 20: "))
            #This condition checks if the user guesses the number
            if PROPOSAL_OF_THE_USER == RANDOM_NUMBER:
                print "You win!"

                RANDOM_NUMBER = random.randint(1, 20) #This generate other random number
                print RANDOM_NUMBER

                ANSWER_WINNER = True
                while ANSWER_WINNER == True: #when the user wins the game asks if want to play again
                    ANSWER_OF_THE_USER = raw_input("Do you want to play again? yes or no:  ")
                    ANSWER_OF_THE_USER = ANSWER_OF_THE_USER.lower()

                    if ANSWER_OF_THE_USER == "yes":
                        ANSWER_WINNER = False #if the answer of the user is "yes" no longer will ask
                        NEW_GAME = True #This will run the game again
                        TURN = True #This will give 4 opportunities to the user
                    elif ANSWER_OF_THE_USER == "no":
                        ANSWER_WINNER = False
                        NEW_GAME = False
                        TURN = 5 #This will stop the game
                        print "Thanks for to play!"
                    else:
                        print "Only can write yes or no  "
                        ANSWER_WINNER = True #The game only can accept "yes" or "no"
            #This compares if the proposal is higher than the generated number
            elif PROPOSAL_OF_THE_USER > RANDOM_NUMBER:
                print "You guessed too high, please try again"
                TURN += 1 #This is for decrease the oportunities
            #This compares if the proposal is lower than the generated number
            elif PROPOSAL_OF_THE_USER < RANDOM_NUMBER:
                print "You guessed too low, please try again "
                TURN += 1
        except NameError: #When the user enters letters
            print "Only can enter numbers "
        except SyntaxError: #When the user enters number with letters
            print "Only can enter numbers "
        except ValueError:
            print "Only can enter numbers "
    #When the user loses the 4 opportunities
    if NEW_GAME == False:
        break
    else:
        print "Game Over"
        print "The number was: %d" % RANDOM_NUMBER
    ANSWER_LOSER = True
    while ANSWER_LOSER == True: #When the user loses the game will ask if want to play again
        ANSWER_OF_THE_USER = raw_input("Do you want to play again? yes or no ")
        ANSWER_OF_THE_USER = ANSWER_OF_THE_USER.lower()

        if ANSWER_OF_THE_USER == "yes":
            ANSWER_LOSER = False
            NEW_GAME = True
        elif ANSWER_OF_THE_USER == "no":
            ANSWER_LOSER = False
            NEW_GAME = False
            print "Thanks for to play "
        else:
            print "Only can write yes or no "
            ANSWER_LOSER = True
