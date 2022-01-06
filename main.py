from random import *
from endScreen import endScreen
from openingScreen import openingScreen
from mainGame import mainGameClass
from init import *
#Creating Objects
openingOBJ = openingScreen()
mainOBJ = mainGameClass() 
closingOBJ = endScreen()
#run the game states in order
openingOBJ.gameState1()
mainOBJ.gameState2()
closingOBJ.gameState3()
    
