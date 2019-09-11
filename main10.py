#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')                 # displays the text Greetings! when you run the program
colors = ['red','orange','yellow','green','blue','violet','purple']  # these are the pool of colors this program is picking from to come up with an answer to the question
play_again = ''                     # lets you play the game again
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): # the two responses to the question play again
    match_color = random.choice(colors)           # choices a color from the pool of colors as the answer to the question
    count = 0                       # counts your number of tries
    color = ''
    while (color != match_color):   # running the main program
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() # how the program reads the answers given to the question
        count += 1                    # count goes up by one each time
        if (color == match_color):    # tells that  the answer is correct
            print('Correct!')         # displays correct on the screen
        else:                         # alternative response to an answer
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #displays Sorry, try again and then how many guesses you have on the screen
    print('\nYou guessed it in {0} tries!'.format(count))   # displays on the screen how many gesses it took you to put in the right answer
    if (count < best_count):          # displays your record of tries
        print('This was your best guess so far!')  # displays a hint
        best_count = count
    play_again = input("\nWould you like to play again? ").lower().strip() # displays Would you like to play again on the screen when you solve the question
print('Thanks for playing!') # displays Thanks for playing on the screen when the game is over