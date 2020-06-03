class CoffeeMachine:
	def __init__(self, water, milk, beans, cups, money):
		self.water = water
		self.milk = milk
		self.beans = beans
		self.cups = cups
		self.money = money

	def current_state(self):
		print('The coffee machine has:')
		print(f'{self.water} of water')
		print(f'{self.milk} of milk')
		print(f'{self.beans} of coffee beans')
		print(f'{self.cups} of disposable cups')
		print(f'{self.money} of money')

	def buy_espresso(self):
		if self.water < 250:
			print('Sorry, not enough water!')
			return
		elif self.beans < 16:
			print('Sorry, not enough coffee beans!')
			return
		elif self.cups < 1:
			print('Sorry, not enough disposable cups!')
			return
		else:
			print('I have enough resources, making you a coffee!')
			self.water -= 250
			self.beans -= 16
			self.cups -= 1
			self.money += 4

	def buy_latte(self):
		if self.water < 350:
			print('Sorry, not enough water!')
			return
		elif self.milk < 75:
			print('Sorry, not enough milk!')
			return
		elif self.beans < 20:
			print('Sorry, not enough coffee beans!')
			return
		elif self.cups < 1:
			print('Sorry, not enough disposable cups!')
			return
		else:
			print('I have enough resources, making you a coffee!')
			self.water -= 350
			self.milk -= 75
			self.beans -= 20
			self.cups -= 1
			self.money += 7

	def buy_cappuccino(self):
		if self.water < 200:
			print('Sorry, not enough water!')
			return
		elif self.milk < 100:
			print('Sorry, not enough milk!')
			return
		elif self.beans < 12:
			print('Sorry, not enough coffee beans!')
			return
		elif self.cups < 1:
			print('Sorry, not enough disposable cups!')
			return
		else:
			print('I have enough resources, making you a coffee!')
			self.water -= 200
			self.milk -= 100
			self.beans -= 12
			self.cups -= 1
			self.money += 6

	def buy_coffee(self):
		print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
		c = input()
		if c == '1':
			self.buy_espresso()

		elif c == '2':
			self.buy_latte()

		elif c == '3':
			self.buy_cappuccino()

		elif c == 'back':
			return

	def fill_supplies(self):
		print('Write how many ml of water do you want to add:')
		w = int(input())
		print('Write how many ml of milk do you want to add:')
		m = int(input())
		print('Write how many grams of coffee beans do you want to add:')
		b = int(input())
		print('Write how many disposable cups of coffee do you want to add:')
		c = int(input())
		self.water += w
		self.milk += m
		self.beans += b
		self.cups += c

	def take_money(self):
		print(f'I gave you ${self.money}')
		self.money = 0

c = CoffeeMachine(400, 540, 120, 9, 550)   
while True:
	print('Write action (buy, fill, take, remaining, exit):')
	action = input()
	if action == 'buy':
		print()
		c.buy_coffee()
		print()
	elif action == 'fill':
		print()
		c.fill_supplies()
		print()
	elif action == 'take':
		print()
		c.take_money()
		print()
	elif action == 'remaining':
		print()
		c.current_state()
		print()
	elif action == 'exit':
		break
