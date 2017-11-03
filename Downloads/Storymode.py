global armor
armor = "none"
def introduction():
	print "Welcome to your story game by Michael Lo, Tim Harlow and Henry Lin. The story is based on the generic princess and dragon stories. Press space and enter to continue."
	answer = raw_input()
	if answer == " ":
		Start()
def Start():
   print "The dragon has taken the princess and the royal family has asked for your help."
   HelpOrNo()

def HelpOrNo(): 
    print "Do you help save the princess?"
    print "Type y for yes and n for no"
    answer = raw_input()
    if answer == "y":
         armortype()
    else:
        print "The End"

def armortype():
    print "Do you need help?"
    print "Type y for yes and n for no"
    answer = raw_input()
    if answer == "y":
        armor = "metal"
    else:
        armor = "leather"
    print "You've been given " + armor + " armor."
    village()

def village():
	print "Go talk to the villager. Do you talk to the one on the left or right?"
	print "Type l for left and r for right"
	answer = raw_input()
	if answer == "l":
		print "Villager: The dragon went to the mountain's summit. Be sure to charge at the dragon with your shield when it spits fire."
	else: 
		print "Villager: The dragon went to the mountain’s summit.  Be sure to hide behind rocks when dragon spits fire."
	mountain()
	
def mountain():
	print "You have reached the summit and are facing the dragon. He prepares to blow fire at you. Do you charge at him or hide? Type c for charge and h for hide."
	answer = raw_input()
	if answer == "c":
		armorcheck()
	#	if answer == "c" and armor == "leather":
#		print "You died. The end."
#	if answer == "c" and armor == "metal":
#		print "You were pushed back by the fire!"
#		survive()
	if answer == "h":
		print "The fire hit the rocks and missed you."
		survive()

def armorcheck():
	if armor == "leather":
		print "You died. The end."
	else:
		print "You were pushed back by the fire!"
		survive()
def survive():
	print "The dragon is out of breath! NOW'S YOUR CHANCE! Do you try to kill it or run for the princess?"
	print "Type k for kill and p for princess"
	answer = raw_input()
	if answer == "k":
		print "You stab the dragon and it dies. You save the princess and live happily ever after."
	else:
		print "The dragon caught its breath because you were too slow! He eats you quickly. The end."
	
introduction()