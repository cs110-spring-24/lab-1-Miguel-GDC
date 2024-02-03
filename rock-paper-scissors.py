import random
cpu = random.randint (1, 3)

user = input ("input rock, paper, or scissors: ")
if user == "rock":
	if cpu == 1: #cpu chose rock
		print("tie game")
	elif cpu == 2: #cpu chose paper
		print("lost game")
	else: 
		print ("won game") 

if user == "paper":
	if cpu == 1:
		print("won game")
	elif cpu == 2: 
		print("tie game")
	else: 
		print("lost game")

if user == "scissors":
	if cpu == 1:
		print("lost game")
	elif cpu == 2:
		print("won game")
	else cpu == 3:
		print("tie game")
