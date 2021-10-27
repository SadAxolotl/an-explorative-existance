#ATTENTION!!!! this is meant to be played by itself, so make a copy and don't run it by yourself so you don't mess up the experiance of others
import os as o
o.system("clear")
import time as t
o.system("clear")
import random as r
o.system("clear")
from playsound import playsound
o.system('clear')
persistant = open("persistant.txt", "r")
o.system("clear")
weapon = open("weapon.txt", "r")
o.system("clear")
with open('version.txt') as vers:
	version = vers.read()
print("WARNING!! this game is in ",version," ,so put bugs in the git, TYTYTY.")
input("press enter to continue...")
o.system("clear")
class swamp:
 swamptf = None
 swamprnd = None
class mtn:
 mtntf = None
 mtnrnd = None
class vars:
 randnum = None
 currh = 20
 kit = 0
 rorl = None
 ifbreak = 0
def dnsw():
	if vars.rorl == "flee":
				chance = r.randint(1,2)
				if chance == 1:
					input("FLEE SUCCESS! hit enter to continue...")
					o.system("clear")
					vars.ifbreak = 1
				else:
					vars.currh -= 3
					print("Oh No! The man runs up to you as you're vunrible and attacks you for 3 health. Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
					o.system("clear")
	elif vars.rorl == "yell":
				chance = r.randint(1,2)
				if chance == 1:
					input("HE IS TERRIFIED, HE RUNS AWAY SCREAMING LIKE A LITTLE GIRL. hit enter to continue...")
					o.system("clear")
					vars.ifbreak = 1
				else:
					vars.currh -= 2
					print("he just pounces at you and takes 2 points away from your health.","Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
					o.system("clear")
	elif vars.rorl == "attack":
				chance = r.randint(1,4)
				if chance == 1:
					input("CRITICAL HIT, YOU TAKE HIM DOWN IN ONE PUNCH, hit enter to continue...")
					o.system("clear")
					vars.ifbreak = 1
				else:
					vars.currh -= 3
					input("He takes the punch and slams you on the ground, you lose 3 health, you are now at: "+str(vars.currh)+", hit enter to continue...")
					o.system("clear")
					vars.ifbreak = 1
	else:
					vars.currh -= 10
					print("What did you just say?! He grabs your punch and throws you to the ground dealing 10 damage!","Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
					o.system("clear")
def swrd():
	print("You got a sword!!")
	weapon = open("weapon.txt", "w")#replace here
	weapon.write("y")
	weapon = open("weapon.txt", "r")#replace here
def swprd():
	swamp.swamprnd = r.randint(1, 5)
def mtnprd():
	mtn.mtnrnd = r.randint(1,6)
def hkit():
	print("You found a healthkit!")
	vars.kit += 1
	yorn = input("type y to use it and n to not use it: ")
	if yorn == "y":
		input("you have used your healthkit, you have gone to maximum health, you now have "+str(vars.kit)+" health kits, hit enter to contiune...")
		vars.currh = 20
		vars.kit -= 1
	else:
		input("you have saved your healthkit, you now have "+str(vars.kit)+" health kits, hit enter to continue...")
	o.system('clear')
def mtndef():
	randnum = r.randint(1,20)
	if randnum == 1 or randnum == 2 or randnum == 3:
		mtn.mtntf = True
		print("you've entered the mountains")
	else:
		mtn.mtntf = False
def swampdef():
	randnum = r.randint(1,20)
	if randnum == 13:
		swamp.swamptf = True
		print("you have entered the swamp")
	else:
		swamp.swamptf = False
def randplay():
	vars.randnum = r.randint(1, 5)
def newplayer():
	persistant = open("persistant.txt", "w")#replace here
	persistant.write("played")
	print("you must be a new player!")
	t.sleep(2)
	print("this is my string based story game that is controlled by multiple choice questions that vary between environments")
	t.sleep(8)
	print("anyways, have fun!")
	t.sleep(3)
	o.system('clear')
	persistant = open("persistant.txt", "r")#replace here
def walk():
	input("you have walked straight because that is the only way, click enter to continue...")
def walkb():
	while True:
		vars.rorl = input("you come at a T in the road, will you go right or left (r or l)")
		if vars.rorl == "r":
			print("you went right")
			break
		elif vars.rorl == "l":
			print("you went left")
			break
def walkc():
	while True:
		vars.rorl = input("you come at a X in the road, will you go right, left, or striaght (r, l, or v)")
		if vars.rorl == "r":
			print("you went right")
			break
		elif vars.rorl == "l":
			print("you went left")
			break
		elif vars.rorl == "v":
			print("you went straight")
			break
def walkd():
	while True:
		if vars.currh < 1:
			death()
		elif vars.ifbreak == 1:
			vars.ifbreak = 0
			break
		vars.rorl = input("you come up to a ravaging man, will you flee (50% success), yell (50% scare success), or attack (25% chance without a weapon, 75 with)\n")
		flag = 0
		for line in persistant:  
			pass
			if "y" in line:
				flag = 1
				break
		if flag == 0:
			dnsw()
		else:
			if vars.rorl == "flee":
				chance = r.randint(1,2)
				if chance == 1:
					input("FLEE SUCCESS! hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 3
					print("Oh No! The man runs up to you as you're vunrible and attacks you for 3 health. Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
					o.system("clear")
			elif vars.rorl == "yell":
				chance = r.randint(1,2)
				if chance == 1:
					input("HE IS TERRIFIED, HE RUNS AWAY SCREAMING LIKE A LITTLE GIRL. hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 2
					input("he just pounces at you and takes 2 points away from your health.","Your health is now down to:",str(vars.currh),"\nhit enter to continue...")
					o.system("clear")
			elif vars.rorl == "attack":
				chance = r.randint(1,4)
				if chance == 1 or 2 or 3:
					input("You stab him in the heart, he bleeds out, hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 20
					print("He grabs your sword and throws you to the ground and stabs you, *CRITICAL HIT* dealing 20 damage!","Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
					o.system("clear")
					break
def walka():
	chance = r.randint(0,5)
	if chance == 0:
		swrd()
		input("YOU FOUND A SWORD!!! hit enter to continue...") 
		o.system("clear")
	else:
		input("you come at a small outpost, you sit down, hit enter to search the area...")
		chance = r.randint(0,3)
		if chance == 0:
			hkit()
def death():
	playsound('dead.mp3')
	print("you died LOL")
	weapon = open("weapon.txt", "w")
	weapon.write("")
	weapon = open("weapon.txt", "r")
	t.sleep(5)
	exit()
def health():
	if vars.currh < 20:
		vars.currh += 1
	else:
		print("you have full health, didn't heal")
def rhealth():
	vars.currh -= 1
	print("it's cold, you lost 1 health, health at "+str(vars.currh))
def s1():
	print("phew,")
	hkit()
def s2():
	while True:
		if vars.currh < 1:
			death()
		vars.rorl = input("you come up to a golem, will you flee (1/4 success), yell (1/8 scare success), or attack (1/5 chance without a weapon, 8/9 with)\n")
		flag = 0
		for line in persistant:  
			pass
			if "y" in line:
				flag = 1
				if vars.rorl == "flee":
					chance = r.randint(1,4)
					if chance == 1:
						input("FLEE SUCCESS! hit enter to continue...")
						o.system("clear")
						break
					else:
						vars.currh -= 15
						print("Oh No! The golem runs up to you as you're vunrible and attacks you for 15 health. Your health is now down to:",str(vars.currh))
						input("hit enter to continue...")
						o.system("clear")
				elif vars.rorl == "yell":
					chance = r.randint(1,8)
					if chance == 1:
						input("HE IS TERRIFIED, HE RUNS AWAY SCREAMING LIKE A LITTLE GIRL. hit enter to continue...")
						o.system("clear")
						break
					else:
						vars.currh -= 10
						print("it just pounces at you and takes 10 points away from your health.","Your health is now down to:",str(vars.currh))
						input("hit enter to continue...")
				elif vars.rorl == "attack":
					chance = r.randint(1,4)
					if chance == 1:
						input("CRITICAL HIT, YOU TAKE IT DOWN IN ONE PUNCH, hit enter to continue...")
						o.system("clear")
						break
					else:
						vars.currh -= 20
						input("it grabs your punch and throws you to the ground dealing 20 damage!","hit enter to continue...")
						o.system("clear")
						break
			else:
				if vars.rorl == "flee":
					chance = r.randint(1,2)
					if chance == 1:
						input("FLEE SUCCESS! hit enter to continue...")
						o.system("clear")
						break
					else:
						vars.currh -= 15
						print("Oh No! The golem runs up to you as 	you're vunrible and attacks you for 15 health. Your health is now down to:",str	(vars.currh))
						input("\nhit enter to continue...")
						o.system("clear")
				elif vars.rorl == "yell":
					chance = r.randint(1,8)
					if chance == 1:
						input("HE IS TERRIFIED, HE RUNS AWAY SCREAMING LIKE A LITTLE GIRL. hit enter to continue...")
						o.system("clear")
						break
					else:
						vars.currh -= 2
						print("he just pounces at you and takes 2 points away from your health.","Your health is now down to:",str(vars.currh))
						input("hit enter to continue...")
						o.system("clear")
				elif vars.rorl == "attack":
					chance = r.randint(1,4)
					if chance == 1:
						input("You slap and kick him, he dies, hit enter to continue...")
						break
						o.system("clear")
					else:
						vars.currh -= 20
						input("He grabs your sword and throws you to the ground and stabs you, *CRITICAL HIT* dealing 20 damage!","Your health is now down to:",str(vars.currh),"\nhit enter to continue...")
						o.system("clear")
						break
		if flag == 0:
			if vars.rorl == "flee":
				chance = r.randint(1,4)
				if chance == 1:
					input("FLEE SUCCESS! hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 15
					print("Oh No! The golem runs up to you as you're vunrible and attacks you for 15 health. Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
					o.system("clear")
			elif vars.rorl == "yell":
				chance = r.randint(1,8)
				if chance == 1:
					input("HE IS TERRIFIED, HE RUNS AWAY SCREAMING LIKE A LITTLE GIRL. hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 10
					print("it just pounces at you and takes 10 points away from your health.","Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
			elif vars.rorl == "attack":
				chance = r.randint(1,4)
				if chance == 1:
					input("CRITICAL HIT, YOU TAKE IT DOWN IN ONE PUNCH, hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 20
					input("it grabs your punch and throws you to the ground dealing 20 damage!","hit enter to continue...")
					o.system("clear")
					break
		else:
			if vars.rorl == "flee":
				chance = r.randint(1,2)
				if chance == 1:
					input("FLEE SUCCESS! hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 15
					print("Oh No! The golem runs up to you as you're vunrible and attacks you for 15 health. Your health is now down to:",str(vars.currh))
					input("\nhit enter to continue...")
					o.system("clear")
			elif vars.rorl == "yell":
				chance = r.randint(1,8)
				if chance == 1:
					input("HE IS TERRIFIED, HE RUNS AWAY SCREAMING LIKE A LITTLE GIRL. hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 2
					print("he just pounces at you and takes 2 points away from your health.","Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
					o.system("clear")
			elif vars.rorl == "attack":
				chance = r.randint(1,4)
				if chance == 1:
					input("You slap and kick him, he dies, hit enter to continue...")
					break
					o.system("clear")
				else:
					vars.currh -= 20
					input("He grabs your sword and throws you to the ground and stabs you, *CRITICAL HIT* dealing 20 damage!","Your health is now down to:",str(vars.currh),"\nhit enter to continue...")
					o.system("clear")
					break
def s3():
	vars.rorl = input("you come up to an abandoned house you can either 'go in' or 'run away'\nwhat will you choose: ")
	o.system("clear")
	if vars.rorl == "go in":
		chance = r.randint(1,3)
		spic = r.randint(1,2)
		if chance == 1:
			input("A spider jumps on you! hit enter to continue...")
			o.system("clear")
			if spic == 1:
				vars.currh -= 10
				input("OH NO! You panic and the spider bites you, you lose 10 health from the poison then leave the house, hit enter to continue...")
				o.system("clear")
			else:
				input("Phew, the spider jumps off of you and you leave the house, hit enter to continue...")
				o.system("clear")
		elif chance == 2:
			while True:
				if vars.currh < 1:
					death()
					break
					vars.rorl = input("you come up to a ravaging man, will you flee (50% success), yell (25% scare success), or attack (15% chance without a weapon, 75% with)\n")
					flag = 0
					for line in persistant:
						pass
					if "y" in line:
						flag = 1
						if flag == 1:
							if vars.rorl == "flee":
								chance = r.randint(1,2)
								if chance == 1:
									input("FLEE SUCCESS! hit enter to continue...")
									o.system("clear")
									break
								else:
									vars.currh -= 3
									print("Oh No! The man runs up to you as you're vunrible and attacks you for 3 health. Your health is now down to:",str(vars.currh))
									input("hit enter to continue...")
									o.system("clear")
							elif vars.rorl == "yell":
								chance = r.randint(1,4)
								if chance == 1:
									input("HE IS TERRIFIED, HE RUNS AWAY SCREAMING LIKE A LITTLE GIRL. hit enter to continue...")
									o.system("clear")
									break
								else:
									vars.currh -= 2
									print("he just pounces at you and takes 2 points away from your health.","Your health is now down to:",str(vars.currh))
									input("hit enter to continue...")
									o.system("clear")
							elif vars.rorl == "attack":
								chance = r.randint(1,20)
								if chance == 1 or 2 or 3:
									input("CRITICAL HIT, YOU TAKE HIM DOWN IN ONE PUNCH, hit enter to continue...")
									o.system("clear")
									break
								else:
									vars.currh -= 10
									input("He grabs your punch and throws you to the ground dealing 10 damage!","Your health is now down to:",str(vars.currh))
									input("hit enter to continue...")
									o.system("clear")
					else:
							if vars.rorl == "flee":
								chance = r.randint(1,2)
								if chance == 1:
									input("FLEE SUCCESS! hit enter to continue...")
									o.system("clear")
									break
								else:
									vars.currh -= 3
									print("Oh No! The man runs up to you as you're vunrible and attacks you for 3 health. Your health is now down to:",str(vars.currh))
									input("hit enter to continue...")
									o.system("clear")
							elif vars.rorl == "yell":
								chance = r.randint(1,4)
								if chance == 1:
									input("HE IS TERRIFIED, HE RUNS AWAY SCREAMING LIKE A LITTLE GIRL. hit enter to continue...")
									o.system("clear")
									break
								else:
									vars.currh -= 2
									input("he just pounces at you and takes 2 points away from your health.","Your health is now down to:",str(vars.currh),"\nhit enter to continue...")
									o.system("clear")
							elif vars.rorl == "attack":
								chance = r.randint(1,5)
								if chance == 1 or chance == 2 or chance == 3 or chance == 4:
									input("You stab him in the heart, he bleeds out, hit enter to continue...")
									break
									o.system("clear")
								else:
									vars.currh -= 20
									print("He grabs your sword and throws you to the ground and stabs you, *CRITICAL HIT* dealing 20 damage!","Your health is now down to:",str(vars.currh))
									input("hit enter to continue...")
									o.system("clear")
									break
		elif chance == 3:
			pra = input("you see a dog in the house, will you 'pet' the dog, 'run', or 'attack' the dog: ")
			o.system("clear")
			if pra == "run":
				input("you escape from the house, hit enter to continue... ")
				o.system('clear')
			elif pra == "pet":
				input("whose a good boy? YOU ARE! you get a sword from the dog! hit enter to continue...")
				swrd()
				o.system('clear')
			elif pra == "attack":
				chance = r.randint(1,4)
				if chance == 1 or chance == 2 or chance == 3:
					input("you think you could get away with trying to kill a dog, you will never prosper, hit enter to continue... ")
					o.system('clear')
					vars.currh = 0
				else:
					input("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO YOU MONSTER, YOU KILLED DOGMEAT! hit enter to continue B(")
					o.system("clear")
			else:
				input("you messed up, hit enter to continue...")
				o.system("clear")
	elif vars.rorl == "run away":
		input("you ran away and survived, hit enter to continue...")
		o.system("clear")
	else:
		input("you messed up, hit enter to continue...")
		o.system("clear")
def s4():
	pass
	o.system('clear')
	yorn = input("you see a woman in the middle of a lake, what will you do ('walk to her','walk away','sneak attack', or 'rush her'")
	if yorn == 'walk to her':
		print("you walk to her")
		t.sleep(.5)
		print("she looks at you")
		for line in persistant:
			pass
		if "y" in line:
			flag = 1
			if flag == 1:
				hkit()
			else:
				swrd()
	elif yorn == 'sneak attack':
		vars.currh = 1
		input("she takes you out in one hit leaving you with 1 health, press enter to continue...")
		o.system('clear')
	elif yorn == 'rush her':
		vars.currh -= 5
		input("she throws you into a tree leaving you with 5 less health, hit enter to continue...")
	else:
		print("you peacfully walk away...")
		t.sleep(5)
		o.system('clear')
def m1():
	yorn = input("OH NO, theres a avalanch, what will you do?!('run', 'hunker down', or 'run into it') ")
	if yorn == 'run':
		chance = r.randint (1,4)
		if chance == 1:
			input("phew, you escaped! hit enter to continue...")
			o.system('clear')
		elif chance == 2:
			vars.currh -= 7
			input ("you lose 7 health from being stuck in the snow then closely after, resqued, press enter to continue...")
			o.system('clear')
		elif chance == 3:
			input("you somehow made it on top of the snow safe, press enter to continue...")
			o.system('clear')
		else:
			print("you got stuck in the snow forever... goodbye...")
			death()
def m2():
	yorn = input("you see a mountain lion in the distance, what will you do ('run away', 'rush', 'sneak attack','befriend'")
	if yorn == 'run away':
		chance = r.randint(1,4)
		if chance == 1:
			input("you ran away, hit enter to continue...")
			o.system('clear')
		else:
			vars.currh -= 15
			input("he catches you and takes 15 health away...")
			print("current health is now "+str(vars.currh))
			o.system('clear')
	elif yorn == 'rush':
		print("the mountain lion hears you and mauls your skin off and eats you to the bone")
		death()
	elif yorn == 'sneak attack':
		chance = r.randint(1,4)
		if chance == 1:
			print("the mtn lion rips you apart, he can easily hear you, rookie.")
			death()
		else:
			input("you kill him in one blow")
def m3():
	pass
def m4():
	pass
def m5():
	pass
while True:
	swampdef()
	mtndef()
	o.system("clear")
	if vars.currh < 1:
		death()
	else:
		flag = 0
		index = 0
		for line in persistant:  
			pass
			if "played" in line:
				flag = 1
				break 
		if flag == 0: 
			newplayer() 
		else: 
			while True:
				if swamp.swamptf == False:
					if vars.kit > 0: 
						hkitvar = input("would you like to use a heath kit (y or n?) you're at "+str(vars.currh)+" health: ") 
						if hkitvar == "y" and vars.kit > 0:
							print("you are now at 20 health!")
							vars.currh = 20
							vars.kit -= 1
							t.sleep(2)
							o.system('clear')
						elif hkitvar == "n":
							print("ok, looks like your not gonna use your kit.")
							t.sleep(2)
							o.system('clear')
						else:
							print("you have no kits")
							t.sleep(2)
							o.system('clear')
					else:
						pass
					health()
					randplay()
					if vars.randnum == 1:
						walk()
					elif vars.randnum == 2:
						walka()
					elif vars.randnum == 3:
						walkb()
					elif vars.randnum == 4:
						walkc()
					elif vars.randnum == 5:
						walkd()
				elif mtn.mtntf == True:
					input("hit enter to continue...")
					o.system('clear')
					while True:
						if vars.currh < 1:
							death()
						else:
							pass
						if r.randint(1,2) == 1:
							health()
						else:
							rhealth()
						if mtn.mtnrnd == 1:
							m1()
						elif mtn.mtnrnd == 2:
							m2()
						elif mtn.mtnrnd == 3:
							m3()
						elif mtn.mtnrnd == 4:
							m4()
						elif mtn.mtnrnd == 5:
							m5()
						else: 
							input("you got out of the mountains!")
							break
				else:
					input("OH CRAP you're in the swamp, hit enter to continue...")
					o.system("clear")
					while True:
						health()
						swprd()
						if vars.currh < 1:
							death()
						if swamp.swamprnd == 1:
							s1()
						elif swamp.swamprnd == 2:
							s2()
						elif swamp.swamprnd == 3:
							s3()
						elif swamp.swamprnd == 4:
							s4()
						elif swamp.swamprnd == 5:
							input("OMG OMG OMG, YOU MADE IT OUT! hit enter to continue..")
							o.system("clear")
							break
				input("hit enter to continue")
				o.system("clear")