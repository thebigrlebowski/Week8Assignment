# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Chris Norman
# Creation Date: 7/28/2021
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time



def displayIntro():   # cleaned up intro so it does not display indents
	print('\nYou are in a land full of dragons. In front of you, you see two caves.')
	print('In one cave, the dragon is friendly and will share his treasure with you.')
	print('The other dragon is greedy and hungry, and will eat you on sight.\n')

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        cave = input('Which cave will you go into? (1 or 2) ')
        if cave != '1' and cave != '2':   #added if statement to let user know if input is incorrect
            print('You messed up. Please try again.')

    return cave  #corrected spelling to cave
		
    
def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	# removed un needed print()
	#sleep for 2 seconds
	time.sleep(4)  # added more time for delay
	
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print ('Gobbles you down in one bite!')   # added () around text

def main():
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y': # corrected to ==
		displayIntro()
		caveNumber = chooseCave()  # corrected spelling error for function call
		checkCave(caveNumber)
    
		playAgain = input('\nDo you want to play again? (yes or no) ').lower()  # changed print to input and added new line to look cleaner. Also added lower function incase user inputs caps.
	
		if playAgain == "no" or playAgain == 'n':  # added n as option like y above
			print("Thanks for playing")  # correct spelling error for playing

main()