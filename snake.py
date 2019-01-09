#coding:utf-8
"""
__version__2.0.2
Version	:			1.0		add evenements plus snake deplacement
					1.1		add analysis (a), info (i), quit(q and red), restart (r) evenements 
					1.2		add random fruit generation (f)
					1.2.5	add the condition for not drawing on the snake during the generation of the fruits
					1.3		add a Rect Map
					1.4		add deltaDeplacement and size to play more pratical 
					1.5		change randint to randrange for fruitAleatoire
					1.5.5	add 4 * marge in fruitAleatoire to correct the position of the fruit during the generation
					1.6		add 1 music when the letter "m" is pressed
					1.6.5	the music is chosen randomly
					1.6.6	the list of musics is set automaticaly  
					1.6.7	add the Coins effect sound when the fruit is eaten
					1.6.8	add the ouch effect when the snake BITE himself
					1.6.9	add the crash effect when the snake hit the board 
					1.7.0	the size of the snake depends on the number of fruit it has eaten 
					1.8.0	add the name of the music below rectMapPlay and the text is center in the middle 
					1.9.0	modification of the size of the rect when the restart button is pushed to keep the name text
							of the music 
					2.0.0	Automatization of the deplacement of the snake
					2.0.1	add the possibility to stop the music when "s" is pushed
					2.0.2	add few comments in fruitAleatoire function and in the main program
__todo__ :	Score enregistré
			Classement des scores

"""
import pygame
import random
import time
import os

#
def fruitAleatoire(xMax, yMax, snakeMap, rayonCercle, yMaxMargeRectMapPlay,marge, nbFruit):
	"""
		:param xMax: the xSize of the windowSurface
		:param yMax: the ySize of the windowSurface
		:param snakeMap: contains all the coordinates of the snake (It is useful for not drawing the food on the snake)
		:param rayonCercle: The radius of the food
		:param yMaxMargeRectMapPlay: To keep a place to put some information
		:param marge: the thikness of the border of the rect
		:param nbFruit: The number of fruits we want 
		:type xMax: INT
		:type yMax: INT
		:type snakeMap: list 
		:type rayonCercle: INT 
		:type yMaxMargeRectMapPlay: INT
		:type marge: INT
		:type nbFruit: INT
		:return: nothing
		:rtype: nothing

		:Example:

		Un exemple écrit après un saut de ligne.

		.. seealso:: main program
		.. warning:: the number of fruits generated is random but it will not exceed nbFruit
					 xMax must be EVEN and yMax must be EVEN too
		.. note:: 
		.. todo:: Must be updated to be more "general"
				  Arrange the randrange to be more "general" 
	"""
	for x in range(1,nbFruit):
		lockDrawFruit	=	False
		xAleatoire	=	random.randrange(rayonCercle +  4 * marge, xMax - rayonCercle,8)
		yAleatoire	=	random.randrange(rayonCercle +  4 * marge, yMax - rayonCercle - yMaxMargeRectMapPlay,8)
		for element in snakeMap:
			if (element[0]-2*rayonCercle < xAleatoire < element[0]+2*rayonCercle) and element[1]-2*rayonCercle < yAleatoire < element[1]+2*rayonCercle:
				lockDrawFruit	=	True		
		if not(lockDrawFruit):
			pygame.draw.circle(mainWindow, blueColor, [xAleatoire,yAleatoire], rayonCercle)	

	pygame.display.flip()


#MAIN PROGRAM
launched			=	True


xMax					=	640 // 2
yMax					=	480 // 2
windowResolution		=	[xMax, yMax]
yMaxMargeRectMapPlay	=	40
margeRectPlay 			=	1
rectMapPlay				=	pygame.Rect(0, 0, xMax-1, yMax-yMaxMargeRectMapPlay)
snakeMap				=	[] 														#Save the coordinates of the snake


rectInfo				=	pygame.Rect(0,yMax-yMaxMargeRectMapPlay+1,xMax-1, yMax-1)
print(type(snakeMap))

redColor			=	(255, 0, 0,255)
blueColor			=	(0, 75, 255,255)
blackColor			=	(0, 0, 0,255)
whiteColor			=	(255, 255, 255,255)
greenColor			=	(0, 255, 0,255)

xDepart				=	xMax//2
yDepart				=	yMax//2

xPos				=	xDepart
yPos				=	yDepart

size				=	8
rayonCercle			=	size // 2
deltaDeplacement	=	8			#must be a multiple of 2
score 				=	0
nbFruit				=	15
gestionDeplacement	=	0
timerEachTicksMs	=	250	

pygame.init()

clock		=	pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, timerEachTicksMs)	

pygame.display.set_caption("SNAKE")
mainWindow	=	pygame.display.set_mode(windowResolution, pygame.RESIZABLE)

ubuntuFont		=	pygame.font.SysFont("ubuntu",15)
musicList		=	os.listdir("/home/user/Documents/PythonTests/Projects/snake/Musics")
musicRepository	=	"Musics/"

soundRepository	=	"SoundForProgramming/"
soundList		=	os.listdir("/home/user/Documents/PythonTests/Projects/snake/SoundForProgramming")
soundCoinsName	=	"Sonic Ring sound Effect in stereo.ogg"
soundOuchName	=	"OUCH Sound Effect!.ogg"
crashSoundName	=	"Broken glass sound effect.ogg"
#dimensionsText	=	ubuntuFont.render("{}".format(windowResolution), True, whiteColor)
#mainWindow.blit(dimensionsText, [10, 10])

#affichage map et debut du serpent 
pygame.draw.rect(mainWindow, greenColor,rectMapPlay, 1)
pygame.draw.circle(mainWindow, redColor, [xPos,yPos], rayonCercle)
pygame.display.flip()
snakeMap.append((xPos,yPos))

pygame.draw.rect(mainWindow, blackColor, rectInfo)
pygame.display.flip()
soundCoins 	=	pygame.mixer.Sound(soundRepository + soundCoinsName)
crashSound 	=	pygame.mixer.Sound(soundRepository + crashSoundName)
ouchSound	=	pygame.mixer.Sound(soundRepository + soundOuchName)

mangerFruit	=	False
while launched:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			launched = False

		elif event.type	==	pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				gestionDeplacement	=	0

			elif event.key ==	pygame.K_DOWN:
				gestionDeplacement	=	1
						
			elif event.key ==	pygame.K_LEFT:
				gestionDeplacement	=	2

			elif event.key ==	pygame.K_RIGHT:
				gestionDeplacement	=	3
			elif event.key == pygame.K_f:
				fruitAleatoire(xMax, yMax, snakeMap, rayonCercle, yMaxMargeRectMapPlay, margeRectPlay, nbFruit)

			elif event.key == pygame.K_r:
				score 		= 0
				pygame.draw.rect(mainWindow, blackColor,rectMapPlay)
				xPos		=	xDepart
				yPos		=	yDepart
				snakeMap[:]	=	[]
				snakeMap.append((xPos,yPos))
				print(snakeMap)
				pygame.draw.rect(mainWindow, greenColor,rectMapPlay, 1)
				pygame.draw.circle(mainWindow, redColor, [xPos,yPos], rayonCercle)
				pygame.display.flip()

			elif event.key == pygame.K_i:
				print("\n[{},{}]".format(xPos, yPos))
				print("----------\n")
				color =	mainWindow.get_at((xPos, yPos))
				print(snakeMap)	
				print("\n--------------\n")
				print(color)
				print("\n--------------\n")
				print(len(snakeMap))

			elif event.key == pygame.K_a:
				for yAnalyse in range(-3,3):
					for xAnalyse in range(-3,3):
						color =	mainWindow.get_at((xPos+xAnalyse, yPos+yAnalyse))
						print(color)
					print("\n")

			elif event.key == pygame.K_m:
				
				randomMusicChoice	=	random.randint(0,len(musicList)-1)
				pygame.mixer.music.load(musicRepository+musicList[randomMusicChoice])
				textMusique			=	ubuntuFont.render(musicList[randomMusicChoice], True, whiteColor)
				dimentionMusic 		=	ubuntuFont.size(musicList[randomMusicChoice])
				pygame.mixer.music.play()
				pygame.draw.rect(mainWindow, blackColor, rectInfo)
				pygame.display.flip()
				mainWindow.blit(textMusique, [(xMax - dimentionMusic[0])//2,(yMax - (yMaxMargeRectMapPlay // 2))])
				pygame.display.flip()
				#pygame.mixer.music.load("/home/user/Musique/JudasPriestLeatherRebel.ogg")

			elif event.key == pygame.K_s:
				pygame.mixer.music.stop()
				pygame.draw.rect(mainWindow, blackColor, rectInfo)
				pygame.display.flip()
			elif event.key == pygame.K_q:
				print("QUIT")
				launched = False
		#Each interrupt move the snake depends on the value of gestionDeplacement
		elif event.type	==	pygame.USEREVENT:
			if(gestionDeplacement	==	0):
				print("HAUT")
				#administration of the deplacement depends on the color of the next move
				if(yPos != deltaDeplacement):
					if (mainWindow.get_at((xPos, yPos - deltaDeplacement)) == blueColor):
						soundCoins.play()
						score += 10
						mangerFruit = True
					elif(mainWindow.get_at((xPos, yPos - deltaDeplacement)) == redColor):
						ouchSound.play()
						time.sleep(1)
						launched	=	False
					score	+= 1
					yPos	-= deltaDeplacement
					snakeMap.append((xPos,yPos))
					if (mangerFruit	== False):
						pygame.draw.circle(mainWindow, blackColor, snakeMap[0], rayonCercle)
						del snakeMap[0]
					print(snakeMap)
					pygame.draw.circle(mainWindow, redColor, [xPos,yPos], rayonCercle)
					pygame.display.flip()
					mangerFruit	=	False
				else:
					crashSound.play()
					time.sleep(1)
					launched	=	False
			if(gestionDeplacement	==	1):
				print("BAS")
				if(yPos != (yMax - yMaxMargeRectMapPlay - deltaDeplacement)):
					if (mainWindow.get_at((xPos, yPos + deltaDeplacement)) == blueColor):
						soundCoins.play()
						score += 10
						mangerFruit = True
					elif(mainWindow.get_at((xPos, yPos + deltaDeplacement)) == redColor):
						ouchSound.play()
						time.sleep(1)
						launched	=	False
					score	+= 1
					yPos	+= deltaDeplacement
					snakeMap.append((xPos,yPos))
					if (mangerFruit	== False):
						pygame.draw.circle(mainWindow, blackColor, snakeMap[0], rayonCercle)
						del snakeMap[0]
					print(snakeMap)
					pygame.draw.circle(mainWindow, redColor, [xPos,yPos], rayonCercle)
					pygame.display.flip()
					mangerFruit	=	False
				else:
					crashSound.play()
					time.sleep(1)
					launched	=	False
			if(gestionDeplacement	==	2):
				print("GAUCHE")
				if(xPos != deltaDeplacement):
					if (mainWindow.get_at((xPos - deltaDeplacement, yPos)) == blueColor):
						soundCoins.play()
						score += 10
						mangerFruit =	True
					elif(mainWindow.get_at((xPos - deltaDeplacement, yPos)) == redColor):
						ouchSound.play()
						time.sleep(1)
						launched	=	False
					score	+= 1
					xPos	-= deltaDeplacement
					snakeMap.append((xPos,yPos))
					if (mangerFruit	== False):
						pygame.draw.circle(mainWindow, blackColor, snakeMap[0], rayonCercle)
						del snakeMap[0]
					print(snakeMap)
					pygame.draw.circle(mainWindow, redColor, [xPos,yPos], rayonCercle)
					pygame.display.flip()
					mangerFruit	=	False
				else:
					crashSound.play()
					time.sleep(1)
					launched	=	False
			if(gestionDeplacement	==	3):
				print("DROITE")
				if(xPos != xMax - deltaDeplacement):
					if (mainWindow.get_at((xPos + deltaDeplacement, yPos)) == blueColor):
						soundCoins.play()
						score += 10
						mangerFruit = True
					elif(mainWindow.get_at((xPos + deltaDeplacement, yPos)) == redColor):
						ouchSound.play()
						time.sleep(1)
						launched	=	False
					score	+= 1
					xPos	+= deltaDeplacement
					snakeMap.append((xPos,yPos))
					if (mangerFruit	== False):
						pygame.draw.circle(mainWindow, blackColor, snakeMap[0], rayonCercle)
						del snakeMap[0]
					print(snakeMap)
					
					pygame.draw.circle(mainWindow, redColor, [xPos,yPos], rayonCercle)
					pygame.display.flip()
					mangerFruit	=	False
				else:
					crashSound.play()
					time.sleep(1)
					launched	=	False

	clock.tick(60)
print("\nSCORE : {}".format(score))

