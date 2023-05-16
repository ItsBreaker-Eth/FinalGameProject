#importing random we need
import random
import pickle
#this is my main branch where i code everything needed in
def ballz():
	print("Welcome to the cave, you have been chosen from your peers to venture in, \nfind the magic stone, and exit the cave safely without losing the stone.")
	print('This your menu, its callable any time by typing "M"')
#this is my menu
	menu = ("""
	||||||||||||||||
	|Menu ------- M|
	|Move Up ---- U|
	|Move Down -- D|
	|Move Left -- L|
	|Move Right - R|
	|Grab Stone - G|
	|Drop Stone - S|
	|Check Cord - C|
	|Quit Game -- Q|
	|Save ---- Save|
	|Load ---- Load|
	||||||||||||||||""")
	print(f"{menu}")

	print("You start at (0,0) Up and Down are Y values, Left and Right are X Values.")
	print("The time has begun for you to begin on your venture through The Maze, good luck, I hope to see you soon.")
#this is defining and classifying the coord that players can call
	XCord = 0
	YCord = 0
	Cord = (f"({XCord}, {YCord})")
	juice = 0
	NewCord = (f"({0}, {0})")
	# Up = YCord += 1
	# Down = YCord -= 1
	# Left = XCord += 1
	# Right = XCord -= 1
#this creates a walls list with everywhere no one can go to.
	walls = []
	while juice < 30:
		temp1 = random.randrange(0,101)
		temp2 = random.randrange(0,101)
		coords = (temp1, temp2)
		walls.append(coords)
		juice += 1


#this sets choice as done
	choice = None
#this chooses the location where the stone will be
	a = random.randint(1,100)
	b = random.randint(1,100)
	
	stone_location = (f"({a},{b})")
#this detects whether they have the stone or not
	stone = False
	spider = 1

	Old_Cord = Cord
#this is what we use for players to make their decisions and movement selections
	while choice != "Q":
		
		choice = input("What is your choice?\n")
		choice = choice.upper()

		if choice == "M":
			print(menu)
		
		elif choice == "U":
			print("You Moved Up")
			YCord += 1
			if (XCord, YCord) in walls:
#this is the code that will print if someone hits a wall and reverts their coord to the old one
				print("You ran into a wall!")
				XCord, YCord = Old_Cord
			else:
				Old_Cord = (XCord, YCord)

		elif choice == "D":
			print("You Moved Down")
			YCord -= 1
			if (XCord, YCord) in walls:
				print("You ran into a wall!")
				XCord, YCord = Old_Cord
			else:
				Old_Cord = (XCord, YCord)


		elif choice == "L":
			print("You Moved Left")
			XCord += 1
			if (XCord, YCord) in walls:
				print("You ran into a wall!")
				XCord, YCord = Old_Cord
			else:
				Old_Cord = (XCord, YCord)


		elif choice == "R":
			print("You Moved Right")
			XCord -= 1
			if (XCord, YCord) in walls:
				print("You ran into a wall!")
				XCord, YCord = Old_Cord
			else:
				Old_Cord = (XCord, YCord)
#players need to use this to try and grab the stone
		elif choice == "G":
			if XCord == a and YCord == b:
				stone = True
				print("You successfully found the Stone! Try and return safely...")
			else:
				print("You are not in the right location! You crabbed a spderz...")
				spider += spider
#this is what players use to drop the stone at the end point
		elif choice == "S":
			if (XCord, YCord) == NewCord:
					print(f"You have completed the game somehow! Congrats!\n You Picked Up {spider} Spiderzzz")
					choice = "Q"
			elif stone is True:
				stone = False
				print(f"You absolute idiot, the stone is magic and teleported away when you dropped it.\nGo find it again.\nYou dropped {spider}")
			else:
				stone = True
				print("Just like in math two negatives equal a positive. \nYou found the stone! \nReturn Safely!")
		elif choice == "C":
			print((f"({XCord}, {YCord})"))
#this is a little cheat for ops to test the code and beat it while also being an easter egg for players to beat it fast.
		elif choice == "OPERATOR COMMAND 69":
			print(walls)
			print(stone_location)
		elif choice == "Q":
			print("Thanks for Playing!")

#the following are the save command for the cords, stone location, and walls
		elif choice == "SAVE":
			print("Your game has been saved.")
			with open("maze_game.dat", "wb") as file:
				pickle.dump((XCord, YCord, stone_location, walls), file)

#this loads the old data
		elif choice == "LOAD":
			print("Your game has been loaded.")
			with open("maze_game.dat", "rb") as file:
				loaded_data = pickle.load(file)
			XCord, YCord, stone_location, walls = loaded_data

		else:
			print("That wasn't an option. Try Again.")

		

















#this runs our main
ballz()