import random
from os import system

# Declaration of global variables
NUM_DIGITS = 0
MAX_GUESSES = 0

# Main menu
def main():
	system("clear")
	print('''Welcome to Bagels, select the mode
By Nicolas Marzagão

Classic Bagels:
	[ 1 ] Classic - Guess the 3 digit number, you have 10 guesses.
	[ 2 ] Mathematician	- Guess the 6 digit number, you have 10 guesses.
	[ 3 ] Genius - Guess the 9 digit number, you have 10 guesses.

Letter Bagels:
	[ 4 ] Classic - Guess the 3 letters, you have 12 guesses.
	[ 5 ] Detective - Guess the 6 letters, you have 12 guesses.
	[ 6 ] Sherlock Holmes - Guess the 9 letters, you have 12 guesses.

Custom Bagels:
	[ 7 ] Set your own challenge.''')

	gamemode = int(input("> "))
	
	# Must init the global variables if you want to modify them
	global NUM_DIGITS
	global MAX_GUESSES
	
	# Switch case to modify game variables and start the game	
	if gamemode == 1: 
		NUM_DIGITS = 3
		MAX_GUESSES = 10
		numGame()
	elif gamemode == 2:
		NUM_DIGITS = 6
		MAX_GUESSES = 10
		numGame()
	elif gamemode == 3:
		NUM_DIGITS = 9
		MAX_GUESSES = 10
		numGame()
	elif gamemode == 4:
		NUM_DIGITS = 3
		MAX_GUESSES = 12
		wordGame()
	elif gamemode == 5:
		NUM_DIGITS = 6
		MAX_GUESSES = 12
		wordGame()
	elif gamemode == 6:
		NUM_DIGITS = 9
		MAX_GUESSES = 12
		wordGame()
	elif gamemode == 7:
		system("clear")
		print('''Custom Bagels - Set Your Own Challenge.
		Please select your type of game:
		[ 1 ] Numbers
		[ 2 ] Letters 
		[ 3 ] Mixed''')
		
		mode = int(input('> '))
		
		print('How many digits/letters should I think of ? ')
		NUM_DIGITS = int(input('> '))
		
		print('How many guesses do you need ? ')
		MAX_GUESSES = int(input('> '))
		
		# switch case to call the choosen gamemode
		if mode == 1:
			numGame()
		elif mode == 2:
			wordGame()
		elif mode == 3:
			mixGame()
		else:
			print("Invalid input exiting game")
		
	else:
		print("Invalid input exiting game")
	
def wordGame():
	system("clear")
	print('''Bagels, a deductive logic game.

I am thinking of {} letters with no repeated letters.
Try to guess what it is. Here are some clues:

When I say:			That means:
	Pico				One letter is correct but in the wrong position.
	Fermi			One letter is correct but in the right position.
	Bagels			No letter is correct.
	
For exmple, if the secret letters were abc and your guess was adb, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

	while True: # Main game loop.
		# This stores the secret number the player needs to guess:
		secretNum = getSecretWord()
		print('I have thought up some letters.')
		print(' You have {} guesses to get it.'.format(MAX_GUESSES))
		
		numGuesses = 1
		while numGuesses <= MAX_GUESSES:
			guess = ''
			# Keep looping untile they enter a valid guess:
			while len(guess) != NUM_DIGITS:
				print('Guess #[{}: '.format(numGuesses))
				guess = input('> ')
				
			clues = getClues(guess, secretNum)
			print(clues)
			numGuesses += 1
			
			if guess == secretNum:
				break # They're correct, so break out of this loop
			if numGuesses > MAX_GUESSES:
				print('You ran out of guesses.')
				print('The answer was {}.'.format(secretNum))
				
		# Ask player if they want to play again
		print('Do you want to play again? (yes or no)')
		if not input('> ').lower().startswith('y'):
			break
	print('Thanks for playing!')
	
def mixGame():
	system("clear")
	print('''Bagels, a deductive logic game.

I am thinking of {} letters and numbers with no repeated digits.
Try to guess what it is. Here are some clues:

When I say:			That means:
	Pico				One digit is correct but in the wrong position.
	Fermi			One digit is correct but in the right position.
	Bagels			No digit is correct.
	
For exmple, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

	while True: # Main game loop.
		# This stores the secret number the player needs to guess:
		secretNum = getMixed()
		print('I have thought up a mixture.')
		print(' You have {} guesses to get it.'.format(MAX_GUESSES))
		
		numGuesses = 1
		while numGuesses <= MAX_GUESSES:
			guess = ''
			# Keep looping untile they enter a valid guess:
			while len(guess) != NUM_DIGITS:
				print('Guess #[{}: '.format(numGuesses))
				guess = input('> ')
				
			clues = getClues(guess, secretNum)
			print(clues)
			numGuesses += 1
			
			if guess == secretNum:
				break # They're correct, so break out of this loop
			if numGuesses > MAX_GUESSES:
				print('You ran out of guesses.')
				print('The answer was {}.'.format(secretNum))
				
		# Ask player if they want to play again
		print('Do you want to play again? (yes or no)')
		if not input('> ').lower().startswith('y'):
			break
	print('Thanks for playing!')

def numGame():
	system("clear")
	print('''Bagels, a deductive logic game.

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:

When I say:			That means:
	Pico				One digit is correct but in the wrong position.
	Fermi			One digit is correct but in the right position.
	Bagels			No digit is correct.
	
For exmple, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

	while True: # Main game loop.
		# This stores the secret number the player needs to guess:
		secretNum = getSecretNum()
		print('I have thought up some letters.')
		print(' You have {} guesses to get it.'.format(MAX_GUESSES))
		
		numGuesses = 1
		while numGuesses <= MAX_GUESSES:
			guess = ''
			# Keep looping untile they enter a valid guess:
			while len(guess) != NUM_DIGITS or not guess.isdecimal():
				print('Guess #[{}: '.format(numGuesses))
				guess = input('> ')
				
			clues = getClues(guess, secretNum)
			print(clues)
			numGuesses += 1
			
			if guess == secretNum:
				break # They're correct, so break out of this loop
			if numGuesses > MAX_GUESSES:
				print('You ran out of guesses.')
				print('The answer was {}.'.format(secretNum))
				
		# Ask player if they want to play again
		print('Do you want to play again? (yes or no)')
		if not input('> ').lower().startswith('y'):
			break
	print('Thanks for playing!')
	
def getSecretNum():
	"""Returns a string made up of NUM_DIGITS unique random digits."""
	numbers = list('0123456789') # Create a list of digits 0 to 9.
	random.shuffle(numbers) # Shuffle them into random order.
	
	# Get the first NUM_DIGITS digits in the list for the secret number:
	secretNum = ''
	for i in range(NUM_DIGITS):
		secretNum += str(numbers[i])
	return secretNum
	
def getSecretWord():
	words = list('qwertyuiopasdfghjklzxcvbnm')
	random.shuffle(words)
	
	secretWord = ''
	for i in range(NUM_DIGITS):
		secretWord += str(words[i])
	return secretWord
	
def getMixed():
	mixed = list('qwertyuiopasdfghjklzxcvbnm0123456789')
	random.shuffle(mixed)
	
	secretMix = ''
	for i in range(NUM_DIGITS):
		secretMix += str(mixed[i])
	return secretMix
	
def getClues(guess, secretNum):
	"""Returns a string with the pico, fermi, bagels clues for a gues and secret 
	number pair."""
	if guess == secretNum:
		return 'You got it!'
	
	clues = []
	
	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			# A correct digit is in the correct place.
			clues.append('Fermi')
		elif guess[i] in secretNum:
			# A correct digit is in the incorrect place.
			clues.append('Pico')
	if len(clues) == 0:
		return 'Bagels' # There are no correct digits at all
	else:
		# Sort the clues into alphabetical order so their original order
		# doesn't give information away
		clues.sort()
		# Make a single string from the list of string clues.
		return ' '.join(clues)
		

# If the program is run (insted of imported), run the game:
if __name__ == '__main__':
	main()		
