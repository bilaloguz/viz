import socket

class VizRT:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

#self.socket.sendall("0 MAIN SHOW_COMMANDS ON\0".encode('ascii'))

    def getVersion(self):
        self.socket.sendall("0 MAIN VERSION\0".encode('ascii'))
        data = self.socket.recv(1024).decode('utf-8')
        return data
    
    def setExternalOn(self):
        self.socket.sendall("0 MAIN SWITCH_EXTERNAL ON\0".encode('ascii'))
        data = self.socket.recv(1024).decode('utf-8')
        return data

    def setExternalOff(self):
        self.socket.sendall("0 MAIN SWITCH_EXTERNAL OFF\0".encode('ascii'))
        data = self.socket.recv(1024).decode('utf-8')
        return data

    def getScenes(self):
        self.socket.sendall("0 SCENE GET_ALL_GROUPS\0".encode('ascii'))
        data = self.socket.recv(1024).decode('utf-8')
        data = data.replace("0 ", "")
        data = data.replace("SCENE", "")
        data = data.replace("*", "")
        scenes = data.split(" ")
        return scenes

    def getObject(self):
        self.socket.sendall("0 RENDERER GET_OBJECT\0".encode('ascii'))
        data = self.socket.recv(1024).decode('utf-8')
        return data # return: '0 #453'

    def getLoadedScene(self):
        self.socket.sendall("0 RENDERER*STAGE*DIRECTOR GET\0".encode('ascii'))
        data = self.socket.recv(1024).decode('utf-8')
        return data # return: '0 #453' (getObject ile aynı şey?)

    def getSceneTree(self):
        self.socket.sendall("0 RENDERER*TREE GET\0".encode('ascii'))
        data = self.socket.recv(1024).decode('utf-8')
        return data # return 0 for now (loaded scene olmamasından ötürü mü?)

    def loadScene(self, scene):
        self.socket.sendall("0 SCENE*".encode('ascii') + scene + " LOAD\0".encode('ascii'))
        data = self.socket.recv(1024).decode('utf-8')
        return data # return: 0 ERROR : the command is not allowed in this mode!!!

    def setScene(self, scene):
        self.socket.sendall("0 RENDERER SET_OBJECT SCENE*".encode('ascii') + scene + "\0".encode('ascii'))
        data = self.socket.recv(1024).decode('utf-8')
        return data

    def getControlChannels(self):
        self.socket.sendall("0 RENDERER*TREE*CONTROL_CHANNEL GET\0".encode('ascii'))
        data = self.socket.recv(1024).decode('utf-8')
        return data # return 0 for now (loaded scene olmamasından ötürü mü?)

    def cleanScene(self):
        self.socket.sendall("0 SCENE CLEANUP\0".encode('ascii'))
        data = self.socket.recv(1024).decode('utf-8')
        return data

    def getSceneInfo(self):
        self.socket.sendall("0 SCENE INFO\0".encode('ascii'))
        data = self.socket.recv(1024).decode('utf-8')
        return data        

scene1 = "STAR_TV/STAR2015/SAHURIFTAR".encode('ascii')
scene2 = "STAR_TV/STAR_2014/DESIGN/IMAGE/REFLECT".encode('ascii')
myViz = VizRT("192.168.147.81", 6100)

#print(myViz.setExternalOn())
#print(myViz.getScenes())
#print(myViz.cleanScene())
#print(myViz.getSceneInfo())
print(myViz.loadScene(scene1))
#print(myViz.loadScene('#453'.encode('ascii')))
#print(myViz.loadScene(scene2))
