"""
Design Pattern - Structural - Proxy

Courtesy of: 
   	- 

Description:
    - 

Learnings: 
	- Use a proxy to do a task

Common Usage:
    - 

"""

def print_header(s):
	print( f"\n#{'-='*35}\n# {s} \n#{'-='*35}")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Proxy
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class RealCmd(object):

    def execute(self, command):
        print( f"Executing : '{command}'" )


class ProxyCmd(object):
    """ 
    Acts as proxy to RealCmd. 
       - Check for admin and user privilages
    """

    def __init__(self, user, previlage ):
        self.is_authorized = True if previlage == "admin" else False
        self.user = user
        self.previlage = previlage

        self.executor = RealCmd()
        self.restricted_commands = ['rm', 'mv']

    def __str__(self):
       return f"{self.previlage}-{self.user}"

    def execute(self, command):
        if self.is_authorized:
            self.executor.execute(command)
        else:
            if any([command.strip().startswith(cmd) for cmd in self.restricted_commands]):
                print(f"ERROR: {self} : '{command}' command is not allowed for non-admin users.")
            else:
                self.executor.execute(command)


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#  Testing  Proxy
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def test_Proxy():

    user  = ProxyCmd("Muni", "user")
    admin = ProxyCmd("Ravi", "admin")

    try:
        admin.execute("ls -la");
        admin.execute("rm -rf /");
        print("\n")
        user.execute("ls -la");
        user.execute("rm -rf");
        user.execute("mv abc xyz");

    except Exception as e:
        print(e)


if __name__ == "__main__":
    test_Proxy()



