from random import *
from openingScreen import openingScreen
from mainGame import mainGameClass
from init import *
#Creating Objects
openingOBJ = openingScreen()
mainOBJ = mainGameClass() 
#run the game states in order
openingOBJ.gameState1()
mainOBJ.gameState2()
    
