import GameObjectsDefinitions

god=GameObjectsDefinitions

#Game State
class GameState():
    def __init__(self):
        self._firstRun = True
        self.isRunning = True
        self.player = god.Player(god.Room,god.Room,"Player1")

def StartGame(state):
    r1 = god.Room(1,None,"The bottom floor...", {})
    r2 = god.Room(2,None, "The first floor...", {})
    r3 = god.Room(3,None, "The top floor...",{})
    r1.AddExit(god.Directions.UP, r2)
    r2.AddExit(god.Directions.DOWN, r1)
    r2.AddExit(god.Directions.UP,r3)
    r3.AddExit(god.Directions.DOWN,r2)
    r1.SetEncounter(god.EncounterTypes.FILE,1,"The last shippment will be at eight.", "_RecordsList")
    r2.SetEncounter(god.EncounterTypes.FILE,3,"Hannah, Richard, Carol, Status: Deceased", "_EncryptedData")
    state.player.SetRoom(r1)
    

def _Accept_Input(command, state):
    command.replace('.', '').replace('?','').replace('!','')
    if command == "quit":
        state.isRunning = False
        return
    god.Actions.AcitonParcer(command,state.player)

#Game Loop
def GameLoop():
    state = GameState()
    
    while state.isRunning:
        if state._firstRun:
            StartGame(state)
            command = input('Enter a command such as go, look and then a direction. ')
            state._firstRun = False
        else:
            command = input('> ')
        _Accept_Input(command, state)
    pass

if __name__ == "__main__":
    GameLoop();
    