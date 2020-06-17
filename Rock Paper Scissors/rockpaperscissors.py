from random import choice

options = []
options2 = []

name = input('Enter your name: ')
print(f'Hello, {name}')
custom_options = input()
if custom_options == '':
	options = ['rock', 'paper', 'scissors']
	options2 = ['rock', 'paper', 'scissors', '!rating', '!exit']
else:
	options = custom_options.split(',')
	options2 = custom_options.split(',')
	options2.extend(['!rating', '!exit'])

score = 0
score_file = open('rating.txt')
for line in score_file:
	n, s = line.split()
	if name == n:
		score = int(s)

print("Okay, let's start")
while True:
	user_choice = input()
	if user_choice == '!exit':
		print('Bye')
		break
	else:
		if user_choice not in options2:
			print('Invalid input')
		elif user_choice == '!rating':
			print(f'Your rating: {score}')
		else:
			computer_choice = choice(options)
			if computer_choice == user_choice: 
				print(f'There is a draw ({computer_choice})')
				score += 50
			else:
				user_choice_index = options.index(user_choice)
				after = options[user_choice_index + 1:]
				before = options[:user_choice_index]
				after.extend(before)
				stronger = after[:len(after) // 2]
				weaker = after[len(after) // 2:]
				if computer_choice in stronger:
					print(f'Sorry, but computer chose {computer_choice}')
				elif computer_choice in weaker:
					print(f'Well done. Computer chose {computer_choice} and failed')
					score += 100
score_file.close()