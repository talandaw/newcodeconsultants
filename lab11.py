# newCode++ Consultants
# Courtney Dunbar, Jordan Horiuchi, Tejus Nandha, Talanda Williams
# CST 205 - Lab 11
# Text-driven adventure game.
# Instuctions appear at the start of the game
# Good luck
#
# Global variables need to be set so functions
# can access the objects stored in them.
 
weapon = 0
gameOver = 0
item = 0
endGame = 0


#Welcome message/instructions displayed at start of game and when user types 'help'
def welcome():
    printNow("Welcome to newCode++ Consultants' Adventure Game!")
    printNow("In each room you will...")
    printNow("You'll be able to go...")
    printNow("Type '<direction>' to move")
    printNow("There are various commands that can be performed on objects")
    printNow("These include: ")
    printNow("Type 'help' to redisplay this intro at any time")
    printNow("Type 'exit' to quit game at any time")

def foyer():
    printNow("----Foyer----")
    printNow("You are in the Foyer.")
    printNow("Add Description")
    printNow("Forward/F - In front of you is the beginning of a hallway, leading to various rooms.")
    printNow("Right/R - To your right is a study.")
    printNow("Left/L - To your left is the living room.")
    printNow("Backward/B - Behind you is the door to the front yard, it seems to be stuck.")
    
    direction = requestString("Which direction will you go?:").lower() 
    if checkInput(direction) != 'exit':   
      if direction == "forward" or direction == "f":
          printNow("Leaving Foyer, Entering Front Hallway...")
          frontHallway()  
      elif direction == "right" or direction == "r":
          printNow("Leaving Foyer, Entering Study...")
          study()
      elif direction == "left" or direction == "l":
          printNow("Leaving Foyer, Entering Living Room...")
          livingRoom()  
      elif direction == "backward" or direction == "b":
          printNow("\nThe Door is Stuck, You are unable to leave...")
          direction = requestString("Which direction will you go?:").lower()           
          #ADD A SECRET ROOM FOR LAB 12?
          #printNow("Leaving house, entering front yard...")
          #frontYard()    
      else:
          printNow("")
          printNow("Improper direction.")
          direction = requestString("Which direction will you go?:").lower()           
        
def study():
    printNow("----Study----")
    printNow("You are in the Study.")
    printNow("Add Description")
    printNow("Forward/F - In front of you is the kitchen.")
    printNow("Left/L - To your left is the foyer.")
    
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':   
       if direction == "forward" or direction == "f":
           printNow("Leaving Study, Entering Kitchen...")
           kitchen()  
       elif direction == "right" or direction == "r":
           printNow("\nSorry, you can't go through the wall.")
           direction = requestString("Which direction will you go?:").lower()           
       elif direction == "left" or direction == "l":
           printNow("Leaving Study, Entering Foyer...")
           foyer()  
       elif direction == "backward" or direction == "b":
           printNow("\nSorry, you can't go through the wall.")
           direction = requestString("Which direction will you go?:").lower()           
       else:
           printNow("")
           printNow("Improper direction.")
           direction = requestString("Which direction will you go?:").lower()           


def livingRoom():
    printNow("----Living Room----")
    printNow("You are in the Living Room.")
    printNow("Add Description")
    printNow("Forward/F - In front of you is jordansRoom.")
    printNow("Right/R - To your right is the foyer.")
    
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':   
       if direction == "forward" or direction == "f":
           printNow("Leaving Living Room, Entering jordansRoom...")
           jordansRoom()  
       elif direction == "right" or direction == "r":
           printNow("Leaving Living Room, Entering Foyer...")
           foyer()
       elif direction == "left" or direction == "l":
           printNow("\nSorry, you can't go through the wall.")
           direction = requestString("Which direction will you go?:").lower()     
       elif direction == "backward" or direction == "b":
           printNow("\nSorry, you can't go through the wall.")
           direction = requestString("Which direction will you go?:").lower()    
       else:
           printNow("")
           printNow("Improper direction.")
           direction = requestString("Which direction will you go?:").lower()           

def frontHallway():
    printNow("----Front Hallway----")
    printNow("You are at the beginning of the hallway.")
    printNow("Add Description")
    printNow("Forward/F - The long dimly light hallway continues.")
    printNow("Right/R - To your right is the kitchen.")
    printNow("Left/L - To your left is jordansRoom.")
    printNow("Backward/B - Behind you is the foyer.")
    
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':
       if direction == "forward" or direction == "f":
           printNow("Walking down the hallway, the lights flicker on and off...")
           backHallway()  
       elif direction == "right" or direction == "r":
           printNow("Entering Kitchen...")
           kitchen()
       elif direction == "left" or direction == "l":
           printNow("Entering jordansRoom...")
           jordansRoom()  
       elif direction == "backward" or direction == "b":
           printNow("Entering Foyer...")
           foyer()
       else:
           printNow("")
           printNow("Improper direction.")
           direction = requestString("Which direction will you go?:").lower()           

def kitchen():
    printNow("----Kitchen----")
    printNow("You are in the Kitchen.")
    printNow("Everything seems dusty except...")
    printNow("There is one clean dish sitting by itself in the dish rack...")
    printNow("Forward/F - In front of you is a bedroom.")
    printNow("Left/L - To your left is the the front hallway.")
    printNow("Backward/B - Behind you is the study.")    
            
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':
       if direction == "forward" or direction == "f":
           printNow("Leaving Kitchen, Entering Main Bedroom...")
           bedroom()
       elif direction == "right" or direction == "r":
           printNow("Opening dish washer...")
           study()
       elif direction == "left" or direction == "l":
           printNow("Leaving Kitchen, Entering Front Hallway...")
           frontHallway()
       elif direction == "backward" or direction == "b":
           printNow("Leaving Kitchen, Entering Study...")
           study()
       else:
           printNow("Improper direction")
           direction = requestString("Which direction will you go?:").lower()           
             
def jordansRoom():
    printNow("----Jordan's Room----")
    printNow("You are in Jordan's Room...")
    printNow("The room is eerily pristine, organized, spotless, aligned...except")
    printNow("Something seems off about this...")
    printNow("Forward/F - In front of you is the guest bedroom.")
    printNow("Right/R - To your right is the front hallway.")
    printNow("Left/L - To your left is a closet.")
    printNow("Backward/B - Behind you is the living room.")
   
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':
       if direction == "forward" or direction == "f":
           printNow("Leaving Jordan's Room, Entering Guest Room...")
           guestRoom()  
       elif direction == "right" or direction == "r":
           printNow("Leaving Jordan's Room, Entering Front Hallway...")
           frontHallway()
       elif direction == "left" or direction == "l":
           printNow("Entering closet...")
           study()  
       elif direction == "backward" or direction == "b":
           printNow("Leaving Jordan's Room, Entering Living Room...")
           livingRoom()
       else:
           printNow("Improper direction.")
           direction = requestString("Which direction will you go?:").lower()           
             
def backHallway():
    printNow("----Back Hallway----")
    printNow("You are in the Back Hallway...")
    printNow("Forward/F, the back door is boarded up.")
    printNow("Right/R - To your right is a bedroom door.")
    printNow("Left/L - To your left is a bedroom door.")
    printNow("Backward/B - Behind you is the front of the hallway.")
    
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':
       if direction == "forward" or direction == "f":
           printNow("You move toward the back door and verify you cannot open it.")
           backHallway() 
       elif direction == "right" or direction == "r":
           printNow("Entering Main Bedroom...")
           bedroom()
       elif direction == "left" or direction == "l":
           printNow("Entering Guest Room...")
           guestRoom()
       elif direction == "backward" or direction == "b":
           printNow("Walking to the front of the hallway...")
           frontHallway()
       else:
           printNow("Improper direction")
           direction = requestString("Which direction will you go?:").lower()           

def bedroom():
    printNow("----Bedroom----")
    printNow("You are in the Main Bedroom...")
    printNow("Be careful, the roof of this room is leaking in few places...")
    printNow("So it is quite slippery in areas")
    printNow("Left/L - To your left is the back hallway.")
    printNow("Backward/B - Behind you is the kitchen.")
    
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':
       if direction == "forward" or direction == "f":
           printNow("\nSorry, you can't go through the wall.")
           direction = requestString("Which direction will you go?:").lower()     
       elif direction == "right" or direction == "r":
           printNow("\nSpend some time to study...")
           study()
       elif direction == "left" or direction == "l":
           printNow("Leaving Bedroom, Entering Back Hallway...")
           backHallway()
       elif direction == "backward" or direction == "b":
           printNow("Leaving Bedroom, Entering Kitchen...")
           kitchen()
       else:
           printNow("Improper direction")
           direction = requestString("Which direction will you go?:").lower()           

def guestRoom():
    printNow("----Guest Room----")
    printNow("You are in the Guest Bedroom...")
    printNow("Spider webs greet you as the door creaks open.")
    printNow("It appears that no one has been in here in AGES.")
    printNow("Right/R - To your right is the back hallway.")
    printNow("Backward/B - Behind you is jordansRoom.")
    
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':
       if direction == "forward" or direction == "f":
           printNow("\nSorry, you can't go through the wall.")
           direction = requestString("Which direction will you go?:").lower()     
       elif direction == "right" or direction == "r":
           printNow("Leaving Bedroom, Entering Back Hallway...")
           backHallway()
       elif direction == "left" or direction == "l":
           printNow("\nSorry, you can't go through the wall.")
           direction = requestString("Which direction will you go?:").lower()    
       elif direction == "backward" or direction == "b":
           printNow("Leaving Guest Room, Entering jordansRoom...")
       else:
           printNow("Improper direction")
           direction = requestString("Which direction will you go?:").lower()           
        
def playGame():
    welcome()
    foyer()       

def checkInput(string):
    if string == "help":
        welcome()
    if string == "exit":
        printNow("\nYou wake up, startled, the house vanishing as a dream...") 
        return 'exit'
      
playGame()