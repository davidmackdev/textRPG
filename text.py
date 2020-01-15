""" 
Another attempt at the TextRPG
"""

import random

QUIT = "QUIT"

WARRIOR = {"Attack": 2,
		   "Heal": 2,
		   "Aglity": 2,
		   "Health": 10,
	   	   "Class": "Warrior"}

BARBARIAN = {"Attack": 3,
		 	 "Heal": 2,
		 	 "Aglity": 1,
		 	 "Health": 15,
	   	   	 "Class": "Barbarian"}

ROUGE = {"Attack": 2,
		 "Heal": 4,
		 "Aglity": 3,
		 "Health": 5,
	   	 "Class": "Rouge"}

ELF = {"Attack": 2,
	   "Heal": 3,
	   "Aglity": 2,
	   "Health": 5,
	   "Race": "Elf"}

DWARF = {"Attack": 3,
		 "Heal": 2,
		 "Aglity": 1,
		 "Health": 15,
	   	 "Race": "Dwarf"}

HUMAN = {"Attack": 2,
		 "Heal": 2,
		 "Aglity": 2,
		 "Health": 10,
	   	 "Race": "Human"}

SWORD = {"Attack": 2,
		 "Aglity": 2,
		 "Weapon": "Sword"}

AXE = {"Attack": 3,
	   "Aglity": 1,
	   "Weapon": "Axe"}

STAFF = {"Attack": 1,
		 "Heal": 3,
		 "Weapon": "Staff"}

player = {"Attack": 1,
		  "Heal": 1,
		  "Aglity": 1,
		  "Health": 10,
		  "Name": "",
		  "Race": "",
		  "Class": "",
		  "Weapon": "",
		  "Type": "Player"}

WITCH = {"Attack": 5,
		 "Heal": 5,
		 "Aglity": 5,
		 "Health": 35,
		 "Name": "The Witch",
		 "Type": "Enemy"}

SEYMOUR = {"Attack": 10,
		   "Heal": 2,
		   "Aglity": 2,
		   "Health": 40,
		   "Name": "Sycamore Seymour",
		   "Type": "Enemy"}



"""
INTRO Functions
"""
def main():
	intro()
	print("\n\tSycamore Seymour: \"My eyes are old and fading warrior, tell me, what are you?\"")
	racePick()
	classPick()
	weaponPick()
	print("\n\tSycamore Seymour: \"Tell me "+ player["Class"] + " " + player["Race"] + "...are you ready to fight the evil?")
	answer = input("\nDo you help Sycamore Seymour?(Y/N) >>> ").upper()
	if answer == 'Y' or answer == "YES":
		print("\nYou have chosen to help Sycamore Seymour.")
		print("\n\tSycamore Seymour: \"Excellent!  I will now tell you of the evil that sourges this land.\n\t\tAn evil Witch cursed parts of the land and turned it unfertile.\n\t\tPlease slay her and set the forest free of her blight.\"\n")
		fight(WITCH)
	elif answer == 'N' or answer == "NO":
		print("\nYou have chosen to abandon Sycamore Seymour.")
		print("\n\tSycamore Seymour: \"Outrage!  You have damned us all then!\n\t\tHave at thee vile Witchkin!\"")
		fight(SEYMOUR)
	

def intro():
	print("\nYou awaken under a large sycamore tree within a lavish green forest.\nSunlight just barely peaks through the think canopy of trees, but you're able to make out how old this area is.\nAs you stand and observe the area, a deep crusty voice breaks the silence:")
	input()
	print("\t???????? ???????: \"Warrior...Warrior!\"")
	input()
	print("You turn to see the tree you were asleep under has a bark knotted face with eyes, a nose and a mouth.\nHis speech is slow and heavy but filled with purpose.")
	input()
	print("\t???????? ???????: \"I am 'The Great Sycamore Tree, Sycamore Seymour.\n\t\tI am the one who has brought you here.\n\t\tTell me warrior, what is your name?\"")
	player["Name"] = input("\nWhat is your name? >>> ")
	print("\n\tSycamore Seymour: \"Ahh...a fine name indeed.  Well then " + player["Name"] + ", \n\t\tI have brought you here to help me slay an evil that curses this land.\n\t\tI promise to send you back after you have finished.\n\t\tYou also have no choice, suck it up.\"")
	input()





"""
Character Customization Functions
"""
def racePick():
	print("\n\nEach race has it's strengths and weaknesses.\nElves heal more damage and move faster, but have less max health and do less damage.\nDwarfs have high damage and max health, but don't heal much damage and move slowly.\nHumans are a balanced race with even stats in everything.")
	race = input("What race are you? >>> ").upper()
	while True:
		if race == "ELF":
			addStat(ELF, race)
			return
		elif race == "HUMAN":
			addStat(HUMAN, race)
			return
		elif race == "DWARF":
			addStat(DWARF, race)
			return
		race = input("Please pick a playable race >>> ").upper()


def classPick():
	print("\n\nEach class has it's strengths and weaknesses.\nRouges heal more damage and move faster, but have less max health and do less damage.\nBarbarians have high damage and max health, but don't heal much damage and move slowly.\nWarriors are a balanced class with even stats in everything.")
	classChoice = input("\nWhat class are you? >>> ").upper()
	while True:
		if classChoice == "WARRIOR":
			addStat(WARRIOR, classChoice)
			return
		elif classChoice == "BARBARIAN":
			addStat(BARBARIAN, classChoice)
			return
		elif classChoice == "ROUGE":
			addStat(ROUGE, classChoice)
			return
		classChoice = input("Please pick a playable class >>> ").upper()

def weaponPick():
	print("\n\nEach weapon has it's strengths and weaknesses.\nStaffs heal more damage but deal less damage.\nThe axe has high damage no healing.\nThe sword is a balanced weapon with even stats in agility and damage.")
	weapon = input("What weapon are you? >>> ").upper()
	while True:
		if weapon == "SWORD":
			addStat(SWORD, weapon)
			return
		elif weapon == "AXE":
			addStat(AXE, weapon)
			return
		elif weapon == "STAFF":
			addStat(STAFF, weapon)
			return
		weapon = input("Please pick a playable weapon >>> ").upper()



def addStat(stats, choice):
	message = ""
	for key in stats:
		if key == "Name": pass
		if key == "Type": pass
		player[key] += stats[key]
		message += "\n" + key + ": " + str(player[key])
	print("As a(n) " + choice.capitalize() + " your stats are:" + message)
	return






"""
Fighting Functions go here
"""
def playerTurn(player, enemy):
	print("It's your turn.\nYou are currently at " + str(player["Health"]) + " HP.") 
	action = input("What would you like to do?(Type ATTACK or HEAL)\n1 -- Attack\n2 -- Heal\n").upper()

	while True:
		if action == "ATTACK": 
			enemy["Health"] -= player["Attack"]
			print(player["Name"] + " has attacked " + enemy["Name"] + " for " + str(player["Attack"]) + "HP.")
			print(enemy["Name"] + " HP: " + str(enemy["Health"]))
			input()
			return
		if action == "HEAL":
			player["Health"] += player["Heal"]
			print("You have healed some minor wounds.")
			print(player["Name"] + " HP: " + str(player["Health"]))
			input()
			return
		action = input("Sorry, that is not a choice.  \nPlease try again >>").upper()

def enemyTurn(enemy, player):
	action = random.randint(1, 2)
	if action == 1: 
		player["Health"] -= enemy["Attack"]
		print(enemy["Name"] + " has attacked " + player["Name"] + " for " + str(enemy["Attack"]) + "HP.")
		print(player["Name"] + " HP: " + str(player["Health"]))
		input()
		return
	if action == 2:
		enemy["Health"] += enemy["Heal"]
		print(enemy["Name"] + " has healed some minor wounds.")
		print(enemy["Name"] + " HP: " + str(enemy["Health"]))
		input()
		return


def fight(enemy):
	if enemy["Aglity"] > player["Aglity"]:
		first = enemy
		second = player
	else:
		first = player
		second = enemy

	count = 1
	print("Round " + str(count) + " against " + enemy["Name"] + " has now begun.  " + first['Name'] + " goes first.")
	input()
	while True:
		if first["Type"] == "Player": 
			print(first)
			playerTurn(first, second)
			if enemy["Health"] <= 0:
				print("You have slain " + enemy["Name"] + ".")
				input()
				return
			if player["Health"] <= 0:
				print("You have been defeated by " + enemy["Name"] + ".")
				input()
				return

			enemyTurn(second, first)
			if enemy["Health"] <= 0:
				print("You have slain " + enemy["Name"] + ".")
				input()
				return
			if player["Health"] <= 0:
				print("You have been defeated by " + enemy["Name"] + ".")
				input()
				return
		else:
			enemyTurn(first, second)
			if enemy["Health"] <= 0:
				print("You have slain " + enemy["Name"] + ".")
				input()
				return
			if player["Health"] <= 0:
				print("You have been defeated by " + enemy["Name"] + ".")
				input()
				return

			playerTurn(second, first)
			if enemy["Health"] <= 0:
				print("You have slain " + enemy["Name"] + ".")
				input()
				return
			if player["Health"] <= 0:
				print("You have been defeated by " + enemy["Name"] + ".")
				input()
				return
		count += 1

	


		


main()