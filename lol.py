			
import random

print("welcome to the dice program")
name = input("What is your name?")
print("Hi, "+name)
score1 = 0
score2 = 0

min_value = 1

max_value = 6


while True:
	guess = input("Do you wanna roll a dice? enter 'y'  or enter 'n' to exit ")
	
	if guess == 'n':
		print("Exitting...")
		break
	
	if guess == 'y':
		
		print("Rolling dices...")
		print("The values are...")
		dice = random.randint(min_value, max_value)
		dice2 = random.randint(min_value, max_value)
		if dice == dice2:
			print("Draw")
		elif dice > dice2:
			print(name+", your result is "+str(dice))
			print("The computer's result is "+str(dice2))
			print(name+", you win!")
			score1 += 1
			print("your current score is "+str(score1))
		elif dice < dice2:
			print(name+", your result is "+str(dice))
			print("The computer's result is "+str(dice2))
			print("Computer wins!")
			score2 += 1
			print("computer's current score is "+str(score2))
		else:
			print("Please enter a valid option")   

		con = input("Do you want to continue or exit(also displays your score), enter 'y' or 'e' only")
		if con == 'y':
			continue
		elif con == 'e':
			print("Your total score is "+str(score1))
			print("The computer's total score is "+str(score2))
			if score1 == score2:
				print("This match is a draw.")
			elif score1 > score2:
				print(name+" wins!")
			elif score1 < score2:
				print("computer wins!")
			else:
				print("Please enter a valid option")
			break
