#
# <Andy Pham>
# <101006098>
#
#<Gaddis, T.(2015). "Starting Out With Python">
#

#Multiple Choice Questions
mc = [["Who is NOT in Super Smash Brothers Melee?", 1, ["Fox", "Sonic", "Donkey Kong"], -1 ,1],
["Which button do you press to use a 'special attack'?", 0, ["B", "A", "Z"], -1, 2],
["Who is the main atagonist of the game?", 1, ["Fox", "Master Hand", "Ganondorf"], -1, 3],
["Which button do you press to grab your opponent?", 2, ["L", "R", "Z"], -1, 4],
["Which stage is NOT in the game?", 0, ["Ottawa", "Final Destination", "Pokemon Stadium"], -1, 5],
["Which Pokemon is NOt in the game?", 0, ["Charmander", "Pikachu", "Mewtwo"], -1, 6],
["Which button do you press to physically attack your opponent?", 2, ["L", "B", "A"], -1, 7],
["Which button do you press to block?", 2, ["L", "R", "Both L or R"], -1, 8],
["What is the maximum amount of stocks you can play with?", 2, ["0", "4", "99"], -1, 9],
["How many people can grab onto an edge or ledge?", 1, ["0", "1", "2"], -1, 10]]

#True or False Questions
tf = [["The game was only made for Gamecube. True or False?", True, -1, 11],
["The game had no prequel or sequel. True or False?", False, -1, 12],
["You can 'Wavedash' in the game. True or False?", True, -1, 13],
["You win by depleting all of the opponent's health bar. True or False?", False, -1, 14],
["You can use items in the game. True or False?", True, -1, 15]]

main = 1

while main == 1: #It repeats the whole quiz program

	#Just as the quiz repeats again, it resets these variables to it's initialized value
	mc_answers = [] 
	tf_answers = []
	correct = 0
	
	print("\n\n******MULTIPLE CHOICE QUESTIONS******") #Header for MC part of quiz

	for loop in range(10): #Loops through entire MC questions
		print("\n\n\nQuestion ", mc[loop][4], ". ", mc[loop][0], sep="")
		print("a.", mc[loop][2][0])
		print("b.", mc[loop][2][1])
		print("c.", mc[loop][2][2])
		print()
		
		mc[loop][3] = input("Type out either (a), (b) or (c): ") #Re-assign the "Player-selected Answer" index equal to the answer you chosen
		
		#Converts letter for worded answer to the index of that answer inside the list of possible of answers
		if mc[loop][3] == 'a' or mc[loop][3] == 'A':
			mc[loop][3] = 0 
		elif mc[loop][3] == 'b' or mc[loop][3] == 'B':
			mc[loop][3] = 1
		elif mc[loop][3] == 'c' or mc[loop][3] == 'C':
			mc[loop][3] = 2
		
		mc_answers.append(mc[loop][3]) #List of MC answers recorded
		
		#If the index is equal to the "Correct Index" index, recieve one mark
		if mc[loop][3] == mc[loop][1]:
			correct = correct + 1
					
		quit = input("\nWould you like to quit? (Type (Y) or (N)): ")
		
		# Stops the "main" loop from looping again, as well as the looping of MC questions
		if quit == "Y" or quit == "y":
			main = 0
			print("Goodbye.")
			break
			

	if len(mc_answers) == 10 and (quit == "N" or quit == "n"): #Safety check if user quits out of MC part, because it'll stop it from going to the TF questions
		print("\n\n\n\n******TRUE OR FALSE QUESTIONS******") #Header for TF part of the quiz
		for loop2 in range(5):
			print("\n\n\nQuestion ", tf[loop2][3], ". ", tf[loop2][0], "\n", sep="")
			tf[loop2][2] = input("Type in (True or T) or (False or F): ") #Re-assign the "Player-selected Answer" index equal to the answer you chose
					
			#Converts answer to its actual Boolean value and overwrites it in the "Player-Selected Answer" index
			if tf[loop2][2] == "False" or tf[loop2][2] == "F" or tf[loop2][2] == "false" or tf[loop2][2] == "f":
				tf[loop2][2] = False
			elif tf[loop2][2] == "True" or tf[loop2][2] == "T" or tf[loop2][2] == "true" or tf[loop2][2] == "t":
				tf[loop2][2] = True
			
			tf_answers.append(tf[loop2][2]) #List of TF answers recorded
			
			#If you get the right answer, recieve one mark
			if tf[loop2][2] == tf[loop2][1]:
				correct = correct + 1
			
			if len(tf_answers) < 5: #Doesn't ask the option to quit now after answering last question
				quit = input("\nWould you like to quit or keep going? (Type (Y) or (N)): ")
				
				# Stops the "main" loop from looping again, as well as the looping of TF questions
				if quit == "Y":
					main = 0
					print("Goodbye.")
					break

					
		#Calculates your score if you COMPLETED every question
		if len(mc_answers) + len(tf_answers) == 15:
			score = (correct/15)*100
					
			print("\n\n\n\n******FINAL SCORE******")
			print("\nYour score is ", score, "%\n", sep="")
			
			retake = input("Would you like to retake the quiz? (Type (Y) or (N)): ")
			
			#Prevents it from looping the entire quiz program again
			if retake == "N" or retake == 'n':
				main = 0
				print("Thank you for taking the test!")
			
		

	
