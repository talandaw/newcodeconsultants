# newCode++ Consultants
# Courtney Dunbar, Jordan Horiuchi, Tejus Nandha, Talanda Williams
# CST 205 - Final Project
# Enhanced text-driven adventure game.
# Instructions appear at the start of the game
import java.awt.Font as Font

# Global variables initialized
userName = ""
items = []
gameCanvas = makeEmptyPicture(800,800)
myFont = makeStyle("Comic Sans", Font.BOLD, 12)
backDoor = makePicture("C://pics/lockedBackDoor.jpg")
frontDoor = makePicture("C://pics/lockedFrontDoor.jpg")
openFrontDoor = makePicture("C://pics/loseHole.jpg")
openBackDoor = makePicture("C://pics/openedFrontDoor.jpg")
lockedBook = makePicture("C://pics/lockedBook.jpg")
unlockedBook = makePicture("C://pics/openedBook.jpg")
crowbar = makePicture("C://pics/crowbar.jpg")
window = makePicture("C://pics/window.jpg")
foyerImage = makePicture("C://pics/foyer.jpg")
studyImage = makePicture("C://pics/study.jpg")
livingRoomImage = makePicture("C://pics/livingRoom.jpg")
frontHallwayImage = makePicture("C://pics/frontHallway.jpg")
libraryImage = makePicture("C://pics/library.jpg")
kitchenImage = makePicture("C://pics/kitchen.jpg")
closetImage = makePicture("C://pics/closet.jpg")
backHallwayImage = makePicture("C://pics/backHallway.jpg")
guestBedroomImage = makePicture("C://pics/guestBedroom.jpg")
masterBedroomImage = makePicture("C://pics/masterBedroom.jpg")

#SOUNDS
backgroundSounds = makeSound("C://sounds/backgroundSounds.wav")
crowbarSound = makeSound("C://sounds/crowbarSound.wav")
doorClosedSound = makeSound("C://sounds/doorClosedSound.wav")
gameOver = makeSound("C://sounds/gameOver.wav")
pickupKeysSound = makeSound("C://sounds/pickupKeysSound.wav")
welcomeSound = makeSound("C://sounds/welcome.wav")
doorClosedSound = makeSound("C://sounds/doorClosedSound.wav") 
openDoor = makeSound("C://sounds/openDoor.wav")
openBook = makeSound("C://sounds/openBook.wav")
windGust = makeSound("C://sounds/windGust.wav")
thud = makeSound("C://sounds/thud.wav")
crowbarTapping = makeSound("C://sounds/crowbarTapping.wav")
cheer = makeSound("C://sounds/cheer.wav")

def pyCopy(source, target, targetX, targetY):
    for x in range (0, getWidth(source)):
        for y in range (0, getHeight(source)):
            color = getColor( getPixel(source, x, y))
            setColor( getPixel(target, targetX + x, targetY + y), color)
    return target
    
#Welcome message/instructions displayed at start of game and when user types 'help'
#The player will attempt to exit an abandoned house through rooms in the house.
#This is a directional text game where the main options are right, left, backward, and forward.
#More options may exist depending on the room the player is in. 
def welcome():
    global userName
    play(welcomeSound)
    showInformation("Welcome to newCode++ Consultants' Adventure Game!\nIn each room you will...\nYou can move forward, backward, left, right, if allowed\nType '<direction>' to move \
    \nThere are various commands that can be performed on specific objects\nThese include: open, use\nType 'help' to redisplay this intro at any time\nType 'exit' to quit game at any time")
    userName = requestString("What is your name, adventurer?:")

#Foyer room description with available directional movement listed
#First room player enters. 
#Forward is the front hallway.
#Right is the study.
#Left is the living room. 
#Backward is the front yard, but the door is now locked. If the player gets the key from the book in the library
#and tries to use it while in the foyer, the key will break and iniate the lose function. 
#The game will then restart.
def foyer():
    global items    
    play(openDoor)
    repaint(foyerImage)
    foyerString = ("----------Foyer---------\nYou are in the Foyer\nThe once grandiose room seems barren now...\nForward/F - In front of you is the Front Hallway, leading to various rooms" +
       "\nRight/R - To your right is a Study\nLeft/L - To your left is the Living Room.\nBackward/B - Behind you is the door to the Front Yard, it seems to be locked, you must need a key.")
    showInformation(foyerString)
    
    #addTextWithStyle( gameCanvas, 50, 600, foyerString, myFont, black)
    #pyCopy(foyerImage, gameCanvas, 0, 0)
    #repaint(foyerImage)
    #gameCanvas = foyerImage
    #repaint(gameCanvas)
    
    #prompt user for string direction/command, convert to all lowercase, compare to available values
    #print appropriate message and, if legal, move in indicated direction
    direction = requestString("Which direction will you go?:").lower() 
    if checkInput(direction) != 'exit':   
        if direction == "forward" or direction == "f":
            showInformation("Leaving Foyer, Entering Front Hallway...")
            frontHallway()  
        elif direction == "right" or direction == "r":
            showInformation("Leaving Foyer, Entering Study...")
            study()
        elif direction == "left" or direction == "l":
            showInformation("Leaving Foyer, Entering Living Room...")
            livingRoom()  
        elif direction == "backward" or direction == "b":
            if "key" in items:
                show(openFrontDoor)
                lose()
            else:
                show( frontDoor)
                play(doorClosedSound)
                showInformation("The Door is locked. You are missing the items to open door...")
                foyer() 
        else:
            showInformation("Improper direction.")
            foyer()         

#Study room description with available directional movement listed  
#There is a broken window in which the player can't fit through. 
#Forward is the kitchen.
#Left is the foyer. 
#There is not a right or backward option, these directions will start the function over.
def study():
    repaint(studyImage) 
    play(windGust) 
    studyString = ("--------Study--------\nYou are in the Study\nA whistling sound startles you when wind comes in through a broken window..." +
        "\nForward/F - In front of you is the Kitchen\nLeft/L - To your left is the Foyer.")
    showInformation(studyString)
    
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':   
        if direction == "forward" or direction == "f":
            showInformation("Leaving Study, Entering Kitchen...")
            kitchen()  
        elif direction == "right" or direction == "r":
            showInformation("Sorry, you can't go through the wall.")
            study()                  
        elif direction == "left" or direction == "l":
            showInformation("Leaving Study, Entering Foyer...")
            foyer()  
        elif direction == "backward" or direction == "b":
            showInformation("Sorry, you can't go through the wall.")
            study()                     
        else:
           showInformation("Improper direction.")
           study()          

#Living Room description with available directional movement listed
#This room is dusty and has not been used for some time. 
#Forward is the library.
#Right is the foyer. 
#Left and backward are not options, they will start the function over.
def livingRoom():
    repaint(livingRoomImage)
    livingRoomString = ("--------Living Room--------\nYou are in the Living Room\nDusty doilies cover various faded couches and chairs..." +
        "\nThis room seems not to have been used for some time\nForward/F - In front of you is Library.\nRight/R - To your right is the Foyer.")
    showInformation(livingRoomString)
    
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':   
        if direction == "forward" or direction == "f":
            showInformation("Leaving Living Room, Entering library...")
            library()  
        elif direction == "right" or direction == "r":
            showInformation("Leaving Living Room, Entering Foyer...")
            foyer()
        elif direction == "left" or direction == "l":
            showInformation("Sorry, you can't go through the wall.")
            livingRoom()       
        elif direction == "backward" or direction == "b":
            showInformation("Sorry, you can't go through the wall.")
            livingRoom()   
        else:
            showInformation("Improper direction.")
            livingRoom()          

#Front Hallway room description with available directional movement listed
#A creepy hallway with portraits on the wall.
#Forward the hallway continues.
#Right is the kitchen.
#Left is the library.
#Backward is the foyer.
def frontHallway():
    repaint(frontHallwayImage)
    frontHallwayString = ("-------Front Hallway--------\nYou are at the beginning of the hallway." +
        "\nPortraits of unknown faces seem to stare at you, questioning why you are in their domain...\nForward/F - The long dimly light hallway continues." + 
        "\nRight/R - To your right is the kitchen.\nLeft/L - To your left is library.\nBackward/B - Behind you is the foyer.")
    showInformation(frontHallwayString)
    
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':
        if direction == "forward" or direction == "f":
            showInformation("Walking down the hallway, the lights flicker on and off...")
            backHallway()  
        elif direction == "right" or direction == "r":
            showInformation("Entering Kitchen...")
            kitchen()
        elif direction == "left" or direction == "l":
            showInformation("Entering library...")
            library()  
        elif direction == "backward" or direction == "b":
            showInformation("Entering Foyer...")
            foyer()
        else:
            showInformation("Improper direction.")
            frontHallway()          

#Kitchen room description with available directional movement listed
#In the kitchen everything is dusty except a plate.
#Forward is a bedroom.
#Left is the front hallway.
#Dishwasher is to the right. Opening the dishwasher gives the player a useful crowbar. This crowbar 
#will be used in the library. A boolean is set to true for the crowbar for later use.
#Backward is the study.
def kitchen():
    global items
    
    repaint(kitchenImage)
    kitchenString = ("--------Kitchen--------\nYou are in the Kitchen.\nEverything seems dusty except...\nThere is one clean dish sitting by itself in the dish rack..." +
        "\nForward/F - In front of you is a bedroom.\nLeft/L - To your left is the the front hallway.\nOpen dishwasher/Open - There is a dishwasher to your right" + 
        "\nBackward/B - Behind you is the study.")    
    showInformation(kitchenString)
                    
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':
        if direction == "forward" or direction == "f":
            showInformation("Leaving Kitchen, Entering Main Bedroom...")
            mainBedroom()
        elif direction == "open dishwasher" or direction == "open":
            show(crowbar)
            play(crowbarSound) 
            showInformation("Opening dish washer...\nYou found a crowbar in the dishwasher that will open the book in the library...")
            items.append("crowbar")
            kitchen()
        elif direction == "left" or direction == "l":
            showInformation("Leaving Kitchen, Entering Front Hallway...")
            frontHallway()
        elif direction == "backward" or direction == "b":
            showInformation("Leaving Kitchen, Entering Study...")
            study()
        else:
            showInformation("Improper direction")
            kitchen()           

#Library room description with available directional movement listed             
#There is a book in the library that looks out of place. 
#If the player gets the book and has the crowbar, the player can open the book and get the key.
#This will change the key value to true.
#If the player gets the book and does not have the crowbar, the book will remain locked.
#The player must go back and get the crowbar from the dishwasher in the kitchn. 
#Forward is the guest bedroom.
#There is an option to open the closet door. The closet is the secret room.
#Backward is the living room.
def library():
    global items
    repaint(libraryImage)
    libraryString = ("--------Library--------\nYou are in the Library...\nThe room is eerily pristine, organized, spotless, aligned...except" +
        "Get book/Get - Something seems off about this book\nForward/F - In front of you is the Guest Bedroom.\nRight/R - To your right is the Front Hallway." + 
        "Open door/Open - To your left is a closed closet door.\nBackward/B - Behind you is the Living Room.")
    showInformation(libraryString)
   
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':
        if direction == "get book" or direction == "get":
            showInformation("As you grab the book, you notice it seems to be hollow and locked, what could be in it?")
            if "crowbar" in items:
                play(pickupKeysSound)
                
                showInformation("You use the crowbar to break the lock on the book...\nInside you find a key for the front and back doors...")
                play(crowbarTapping)
                play(openBook)
                show(unlockedBook)
                items.append("key")
            else:
                show(lockedBook)
                showInformation("You are missing the required item to open the book...")
            library()  
        elif direction == "forward" or direction == "f":
            showInformation("Leaving Library, Entering Guest Room...")
            guestBedroom()  
        elif direction == "right" or direction == "r":
            showInformation("Leaving Library, Entering Front Hallway...")
            frontHallway()
        elif direction == "open door" or direction == "open":
            showInformation("Attempting to open closet door...")
            if "key" in items:
                showInformation("You use the key to unlock the door")
                
                closet()
            else:
                showInformation("The closet door is firmly shut.")
                library()
        elif direction == "backward" or direction == "b":
            showInformation("Leaving Library, Entering Living Room...")
            livingRoom()
        else:
            showInformation("Improper direction.")
            library()          

#Closet (Bonus Room) description with available directional movement listed 
#the closet can only be accessed through the library. 
#The clue for the key is on the diary. The front of the diary has the word "FEAR" on it
#referencing fear the front door. The back of the diary has the word "CLEAR" on it referencing
#the back door is clear to use.
#Backward is the library and the only way out of the closet. All other directions are improper
#directions.
def closet():
    repaint(closetImage)
    play(openDoor)
    closetString = ("--------Secret Room: Closet--------\nYou are in a Closet in the Library...\nFlicking on a light: You pick up a diary, which details the origins of the house." +
        "There was a happy family here.. in 1902. There is no description on where they went.\nScribbled on the front is the word: FEAR\nScribbled on the back is the word: CLEAR" +
        "Backward/B - Behind you is the Library")
    showInformation(closetString)
    
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':
        if direction == "backward" or direction == "b":
            showInformation("The closet light flickers off, and you wonder how there was power in the first place.")
            showInformation("You back out of the closet and return to the library...")
            library()
        else:
            showInformation("Improper direction")
            closet()
            
#Back Hallway room description with available directional movement listed  
#The backHallway is at the back of the house and last room the player will enter before winning.
#Foward is a boarded up door that can be accessed if the player has the key. This will win the game.
#If the player does not have the key, the player continues playing. 
#To the right is the main bedroom.
#Backward is the front hallway.
#Left is the guest room
def backHallway():
    repaint(backHallwayImage)
    backHallwayString = ("--------Back Hallway--------\nYou are in the Back Hallway...\nForward/F, the Back Door is boarded up." +
         "\nRight/R - To your right is the Main Bedroom door.\nLeft/L - To your left is the Guest Bedroom door.\nBackward/B - Behind you is the Front Hallway.")
    showInformation(backHallwayString)
    
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':
        if direction == "forward" or direction == "f":
            showInformation("You move toward the back door and verify it is locked.")
            if "key" in items:
                showInformation("You use the key to open the Back Door")
                show(openBackDoor)
                win()
            else:
                show(backDoor)
                showInformation("You are missing the key to unlock the door..")
                backHallway() 
        elif direction == "right" or direction == "r":
            showInformation("Entering Main Bedroom...")
            mainBedroom()
        elif direction == "left" or direction == "l":
            showInformation("Entering Guest Room...")
            guestBedroom()
        elif direction == "backward" or direction == "b":
            showInformation("Walking to the front of the hallway...")
            frontHallway()
        else:
            showInformation("Improper direction.")
            backHallway()   

#Main bedroom description with available directional movement listed 
#The mainBedroom is leaky.
#To the left is the back hallway.
#Backward is the kitchen.
#Right sends the player back to the study.
#Forward is not an option and restarts the function.
def mainBedroom():
    repaint(masterBedroomImage)
    play(openDoor)
    
    mainBedroomString = ("--------Main Bedroom--------\nYou are in the Main Bedroom...\nThe roof of this room is leaking in few places..." +
        "Left/L - To your left is the back hallway.\nBackward/B - Behind you is the kitchen.")
    showInformation(mainBedroomString)
    
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':
        if direction == "forward" or direction == "f":
            showInformation("Sorry, you can't go through the wall.")
            mainBedroom() 
        elif direction == "left" or direction == "l":
            showInformation("Leaving Main Bedroom, Entering Back Hallway...")
            backHallway()
        elif direction == "backward" or direction == "b":
            showInformation("Leaving Main Bedroom, Entering Kitchen...")
            kitchen()
        else:
            showInformation("Improper direction.")
            mainBedroom()           

#Guest Room description with available directional movement listed   
#The guestBedroom is full of spider webs and has not been used in ages.
#Right is the back hallway.
#Backward is the library.
#Foward is not an option and restarts the function.
#Left allows player to peer through a window, but then black out and the function restarts.
def guestBedroom():
    repaint(guestBedroomImage)
    
    guestBedroomString = ("--------Guest Bedroom--------\nYou are in the Guest Bedroom...\nSpider webs greet you as the door creaks open." +
        "It appears that no one has been in here in AGES.\nRight/R - To your right is the back hallway.\nLeft/L - To your left is a window, maybe it will open." +
        "\nBackward/B - Behind you is library.")
    showInformation(guestBedroomString)
    
    direction = requestString("Which direction will you go?:").lower()
    if checkInput(direction) != 'exit':
        if direction == "forward" or direction == "f":
            showInformation("Sorry, you can't go through the wall.")
            guestBedroom() 
        elif direction == "right" or direction == "r":
            showInformation("Leaving Guest Bedroom, Entering Back Hallway...")
            backHallway()
        elif direction == "left" or direction == "l":
            show(window)
            showInformation("You peer towards a window on the left side of the room before blacking out momentarily.")
            play(thud)
            guestBedroom()
        elif direction == "backward" or direction == "b":
            showInformation("Leaving Guest Bedroom, Entering library...")
            library()
        else:
            showInformation("Improper direction")
            guestBedroom()
 
#Player wins if the crowbar is used to open the book and the key inside the book is used to unlock the backdoor. 
#Player can only win in the backhallway.
def win(): 
    play(cheer)
    showInformation("Congratulations, " + userName + "!!!\nYou successfully exited the house and completed the game!")
    
#Player loses if the key in the book is used in the front door. The key breaks off and the player does not 
#have a way out.
#Player can only lose in the foyer.
def lose():
    play(gameOver) #Game over vocal
    showInformation("GAME OVER, " + userName + "!\nYour key broke in the door. You are trapped forever!")
    #playGame()

#Main game function invokes the welcome message and then starts the user in the foyer       
def playGame():
    welcome()
    foyer()       

#helper function which will check if the user inputs exit of help
def checkInput(string):
    if string == "help" or string == "h":
        welcome()
        return "welcome"
    if string == "exit" or string == "e":
        showInformation("You wake up, startled, the house vanishing as a dream...") 
        return "exit"
      
playGame()

