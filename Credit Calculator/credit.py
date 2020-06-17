import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--type', help='Type of Credit Repayment')
parser.add_argument('--principal', help='Principal Amount', type=int)
parser.add_argument('--payment', help='Monthly Payment Amount', type=float)
parser.add_argument('--interest', help='Annal Interest Rate', type=float)
parser.add_argument('--periods', help='Count of Months', type=int)
args = parser.parse_args()
if len(sys.argv) < 5:
	print('Incorrect parameters')
else:
	repayment_type = args.type
	principal = args.principal
	payment = args.payment
	interest = args.interest
	periods = args.periods
	if repayment_type == None or repayment_type not in ['diff', 'annuity']:
		print('Incorrect parameters')
	elif interest == None or interest < 0:
		print('Incorrect parameters')
	else:
		if repayment_type == 'diff':
			if principal == None or principal < 0:
				print('Incorrect parameters')
			elif periods == None or periods < 0:
				print('Incorrect parameters')
			elif payment != None:
				print('Incorrect parameters')
			else:
				print('Calculating Differentiated Payment')
				total_payment = 0
				i = interest / (12 * 100)
				for m in range(1, periods + 1):
					monthly_payment = math.ceil((principal / periods) + i * (principal - (principal * (m - 1) / periods)))
					print(f'Month {m}: paid out {monthly_payment}')
					total_payment += monthly_payment
				print(f'\nOverpayment = {total_payment - principal}')
		elif repayment_type == 'annuity':
			i = interest / (12 * 100)
			if periods == None:
				if principal < 0:
					print('Incorrect parameters')
				elif payment < 0:
					print('Incorrect parameters')
				else:
					count_months = math.ceil(math.log(payment / (payment - (i * principal)), 1 + i))
					years = count_months // 12
					months = count_months % 12
					if years == 0:
						if months == 1:
							print(f'You need {months} month to repay this credit!')
						else:
							print(f'You need {months} months to repay this credit!')
					elif months == 0:
						if years == 1:
							print(f'You need {years} year to repay this credit!')
						else:
							print(f'You need {years} years to repay this credit!')
					else:
						print(f'You need {years} years and {months} months to repay this credit!')
					print(f'Overpayment = {math.ceil(count_months * payment - principal)}')
			elif payment == None:
				if periods < 0:
					print('Incorrect parameters')
				elif principal < 0:
					print('Incorrect parameters')
				else:
					payment = math.ceil(principal * ((i * math.pow(i + 1, periods)) / (math.pow(i + 1, periods) - 1)))
					print(f'Your annuity payment = {payment}!')
					print(f'Overpayment = {math.ceil(periods * payment - principal)}')
			elif principal == None:
				if periods < 0:
					print('Incorrect parameters')
				elif payment < 0:
					print('Incorrect parameters')
				else:
					principal = payment / ((i * math.pow(i + 1, periods)) / (math.pow(i + 1, periods) - 1))
					print(f'Your credit principal = {math.floor(principal)}!')
					print(f'Overpayment = {math.ceil(periods * payment - principal)}')