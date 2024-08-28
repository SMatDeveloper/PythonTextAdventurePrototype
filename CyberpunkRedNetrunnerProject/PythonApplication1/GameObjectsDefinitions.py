
from enum import Enum
from abc import ABC
import random

class EncounterTypes(Enum):
    EMPTY = 0
    FILE = 1
class Directions(Enum):
    DOWN = 0
    UP = 1
class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    IMPOSSIBLE = 4
class Room:
    def __init__(self, roomPos, encounter, description,exits):
        #the room pos should contain an integer used when generating a level.
        self.roomPos = roomPos
        self.encounter = None
        self.description = description
        self.exits = {}
    def SetEncounter(self, eT, enDifficulty, filetext,name):
        
        if eT == EncounterTypes.FILE:
            new_encounter = FileEncounter(Difficulty, False,filetext,name)
        elif eT == EncounterTypes.EMPTY:
            #print("Encounter None")
            return
        else:
            new_encounter = Encounter(Difficulty,False)
        new_encounter.SetDifficulty(Difficulty(enDifficulty))
        self.encounter = new_encounter
    def isEncounterDone(self):
        if self.encounter.done:
            print("EncounterFinished")
        return self.encounter.done
    def AddExit(self, _exitDir, room):
        self.exits[_exitDir] = room
        #add the exit from directions enum
        pass
    def GetExits(self):
        return self.exits 
        
        
class Player:
    def __init__(self, currentRoom, lastRoom ,name):
        self.currentRoom = None
        self.lastRoom = None
        self.name = name
        
    def SetRoom(self,room):
        self.lastRoom = self.currentRoom
        self.currentRoom = room
        #print(self.currentRoom.description)
        pass 

class Encounter:
    def __init__(self, difficulty, done):
        self.difficulty = Difficulty
        self.done = False
    def SetDifficulty(self, new_difficulty):
        if isinstance(new_difficulty, Difficulty):
            self.difficulty = new_difficulty
        else:
            print("invalid difficulty")
    def DV(self):
        dv = 0
        if self.difficulty.value == 1:
            dv = 10
            print(f"Difficulty Value: {dv}")
            
        elif  self.difficulty.value == 2:
                        dv = 15
                        print(f"Difficulty Value: {dv}")
                        
        elif self.difficulty.value == 3:
                    dv = 20
                    print(f"Difficulty Value: {dv}")
                    
        elif self.difficulty.value == 4:
                    dv = 30
                    print(f"Difficulty Value: {dv}")
                    
        else:
            dv = 0
        return dv
#extention of Encounter
class FileEncounter(Encounter):
    def __init__(self, difficulty,done, contents, name):
        super().__init__(difficulty,done)
        self.contents = contents
        self.name = name
    def DecypherFile(self, bonus):
        rollresult = random.randint(1,10)
        if rollresult == 1:
            print("fumble...")
            rollresult -= random.randint(1,10)
        elif rollresult == 10:
            print("Critical Bonus!")
            rollresult += random.randint(1,10)
        if(rollresult + bonus < self.DV()):
            print(f"You could not decypher the file... {rollresult + bonus}")
            self.done = True
            return False
        else:
            print(f"You Decypher the file... {rollresult + bonus}")
            return True 
    def ReadFile(self):
        if self.done == False:
            #print(self.contents)
            self.done = True
            return self.contents
#this class stores a long string of information which is readable if you pass a dificulty check.

class PasswordEncounter(Encounter):
    pass

class Actions:
    #parse action
    def AcitonParcer(command, p):
         if not command:
             return 
         
         tokens = command.lower().split()
         action = tokens[0]
         
         if action == "go" or action == "move" and len(tokens) > 1:
             direction = tokens[1]
             #initiate the action with the direction
             Actions.Go_Action(direction, p)
         elif action == "look" or action == "search":
             Actions.Look_Action(p) 
         elif action == "use" or action == "inspect":
             Actions.Interact_Action(p) 
         else:
             print("Invalid Action Please type Go or Move and then a direction, Up or Down") 
    #do action         
    def Go_Action(direction, player):
        print(f"Going {direction} From {player.currentRoom.description}.")
        curRoom = player.currentRoom
        ExitPaths = curRoom.GetExits()
        if direction == "up":
              #check the current room if it has an exit in the up direction
              if contains_Direction_Type(ExitPaths, Directions.UP):
                  player.SetRoom(ExitPaths[Directions.UP]) 
              else:
                  print("Failed to move room...") 
        elif direction == "down":
            if contains_Direction_Type(ExitPaths,Directions.DOWN):
                  player.SetRoom(ExitPaths[Directions.DOWN])  
            else:
                  print("Failed to move room...")
        else:
            print("direction entered was invalid. Please enter a valid direction after entering go...") 
            
    def Interact_Action(player):
        if player.currentRoom.encounter == None:
            print("You cannot do that here...")
            return
        encounter = player.currentRoom.encounter
        if player.currentRoom.isEncounterDone():
            print("There is nothing else here...")
            return 
        if isinstance(encounter, FileEncounter):
             if encounter.DecypherFile(9) == True:
                  txt = encounter.ReadFile();
             else:
                 txt = "Co/RRup??--Ted" 
             print(f"Attempting to interact with {encounter.name}. \nIt contains: {txt}") 
                  
    def Look_Action(player):
        curRoom = player.currentRoom
        print(f"You look around {curRoom.description}")
        if curRoom.encounter == None:
            print("You don't see anything of interest...") 
            return
        if curRoom.isEncounterDone():
            print("You already got what was here.") 
            return
        if isinstance(curRoom.encounter, FileEncounter):
            print("There is an Unknown File...") 
        
             
        
       
              
    
              
def contains_Direction_Type(dictionary, enumKey):
         return enumKey in dictionary             
  



