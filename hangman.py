from random import choice
import string

print('H A N G M A N')
words = ['python', 'java', 'kotlin', 'javascript']
correct = choice(words)
list_correct = list(correct)
dashes = '-' * len(correct)
attempts = 1
entered = set()
while True:
	option = input('Type "play" to play the game, "exit" to quit: ')
	if option == 'exit':
		break
	elif option == 'play':
		while attempts <= 8:
			print()
			print(dashes)
			dashes = list(dashes)
			letter = input('Input a letter: ')
			if len(letter) != 1:
				print('You should input a single letter')
			else:
				if letter in entered:
					print('You already typed this letter')
				else:
					entered.add(letter)
					if letter not in string.ascii_lowercase:
						print('It is not an ASCII lowercase letter')
					else:
						if letter in list_correct:
							for c in range(len(correct)):
								if letter == list_correct[c]:
									dashes[c] = letter
							if dashes == list_correct:
								print(f"You guessed the word {''.join(dashes)}!")
								print('You survived!')
								break
						else:
							print('No such letter in the word')
							if attempts == 8:
								print('You are hanged!')
								break
							else:
								attempts += 1
			dashes = ''.join(dashes)
		print()