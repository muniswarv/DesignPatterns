"""
Design Pattern - Behavioural - Command
    - Encapsulate the request on an object. 

Reference of: 
   	- Book:  Head First Design Patterns by Eric Freeman.
	- 

Guiding Principles:
    - Decouple the requester of an action from the object that actually performs the action
    - Terminology
        - Invoker : Invokes the command, like remoteController 
        - Client  : Comments with object, like Device API
        - Executor : Command/method in client that execute the task
    - Invoker has to issue a command and doesn't care about what the Executer does.
    - All objects should have single execute/interface command
    - Command packages the actions and the receiver up into an object that exposes just one method, execute()

Description:

Learnings: 

"""

def print_header(s):
	print( f"\n#{'-='*35}\n# {s} \n#{'-='*35}")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Command : Home Automation - Remote 
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""
Home Automation Remote Control:
   - Have a remote with 4 device connections
   - Each device will have on/incr and off/Decr button
   - User can configure a device to each switch
"""
Class NoCommand(object):

    def __init__(self, name):
        self.name  = name

    def execute(self, switchOn=True, switchOff=False):
        pass


Class SmartFanControl(object):
    maxSpeed = 5
    
    def __init__(self, name):
        self.name  = name
        self.speed = 0
    
    def __str__(self):
        return f"{self.__class__.__name__}:{self.name}"

    def _incrSpeed(self):
        if self.speed < self.maxSpeed: self.speed += 1

    def _decrSpeed(self):
        
        if self.speed > 0: 
            self.speed -= 1
        else:
            self.state = "off"

    def execute(self, switchOn=True, switchOff=False):

        if switchOn : self._incrSpeed()
        if switchOff: self._decrSpeed()


Class SmartTVControl(object):
    maxSpeed = 5
    
    def __init__(self, name):
        self.name  = name
        self.state = "off"
        
    def __str__(self):
        return f"{self.__class__.__name__}:{self.name}"

    def _turnOn(self):
        self.state = "on"

    def _turnOff(self):
        self.state = "on"

    def execute(self, switchOn=True, switchOff=False):

        if switchOn : self._turnOn()
        if switchOff: self._turnOff()


Class GarderSprinklerControl(object):

    maxMoisture = 5 
    minMoisture = 1  
    
    def __init__(self, name):
        self.name  = name
        self.moisture = 0
        self.moter    = "off"

    def __str__(self):
        return f"{self.__class__.__name__}:{self.name}"
     
    def _getMoisture(self):
        return self.moisture

    def _turnOn(self):

        if self.moisture < self.maxMoisture:
            self.moter = "on"
            print( f"Turned on Sprinkler at '{self}'")
        else:
            print( f"Soil at '{self}' is moisture is good enough. No need to turn on moter")

    def _turnOff(self):
        self.state = "off"
        print( f"Turned off Sprinkler at '{self}'")

    def execute(self, switchOn=True, switchOff=False):

        if switchOn : self._turnOn()
        if switchOff: self._turnOff()




#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#  Invoker
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Class RemoteController(object):

    MAX_DEVICES = 4

    def __init__(self, name):
        self.name  = name
        self.commands = [ NoCommand(f"switch{i}" for i in range(self.MAX_DEVICES) )]

    def setCommand(self, index, cmd):
        self.command[index] = cmd

    def switchOn(self, index):
        self.commands[index].execute()


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#  Testing  Command
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def test_Command():
	pass



if __name__ == "__main__":
	test_Command()



