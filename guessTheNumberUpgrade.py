# Kristina Beck
import random

# -------------------------------------------------------------------
# this is the generateNumber function
# it has one parameter:
#   'topLimit' which is the top limit for the random number generator
# the function returns the random number generated to its caller
def generateNumber( topLimit ):
    generateNumber = int(input())   

    
# end of generateNumber function -------------------------------------
# -------------------------------------------------------------------
# this is the askUserToGuess function
# it has two parameters:
#   the 'times' parameter is the number of guesses allowed
#   the 'secretNumber' parameter is the secret, random number
# the function returns one of two values:
#   return True if the user guessed the answer correctly
#   return False if the user did not guess the answer correctly
def askUserToGuess( times, secretNumber ):

    # this loop cycles through all the user guesses
    for guessesTaken in range(1, times+1):
        print('Take your guess #' + str(guessesTaken) + ': ')
        guess = int(input())

        if evaluateAnswer( guess, secretNumber ) == True:
            return True

    return False
# end of askUserToGuess function ----------------------------------


# -------------------------------------------------------------------
# this is the evaluateAnswer function
# it has two parameters:
#   the 'userGuess' parameter is the answer entered by the user
#   the 'userSecretNumber' parameter is the randomly generated number
def evaluateAnswer( userGuess, userSecretNumber ):

    if userGuess < userSecretNumber:
        print ( 'Your guess is too low.' )
    elif userGuess > userSecretNumber:
        print ( 'Your guess is too high.' )
    else:
        return True
   

    

    

# end of evaluateAnswer function -------------------------------------
# -------------------------------------------------------------------
# this is the playGame function
# it has one parameter:
#   'showAnswer' is a Boolean value, if that Boolean value is:
#       True, we'll show the right answer on the screen
#       False, we won't show the right answer on the screen
def playGame( showAnswer ):
    
    print ('Hello. This is a random number guessing game')

    print ('Pick the upper limit:')
    upperLimit = int(input())
    print ('Choose the total number of guesses.')
    totalGuesses = int(input())
    theNumber = random.randint(1, upperLimit)


    print ('Guess a number between 1 and ' +  str(upperLimit) +'. You have ' + str(totalGuesses)+ ' guesses.')
#
    
    # you don't need to change anything below this comment ##############
    # ///////////////////////////////////////////////////////////////////
    # this if statement allows us to show the hidden number to the user
    if( showAnswer == True ):
        print('--shhh, the real number is ' + str(theNumber) + '.')
    
    #this gives a sucess/fail message if the user guessed correctly in the allotted attempts
    if askUserToGuess(totalGuesses,theNumber) == True:
        print('Good job! You guessed my number!')
    else:
        print('Nope. The number I was thinking of was ' + str(theNumber))
playGame(True)
# end of playGame function -----------------------------------------
