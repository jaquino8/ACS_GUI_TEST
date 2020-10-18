import tkinter as tk
import math

class DEC:
    def __init__(self, TopWindow):
        
        self.TopWindow = TopWindow

        self.bindEvents()

        # dictionairy of lines
        # { "LineID": [List of points on the line], ..., "LineIDX" :[]}
        # point format: ((x, y), (B, G, R))
        self.lines = dict() 

        pointCollections = None # should be a collection of points

    def bindEvents(self):

        self.TopWindow.LeftControlPanel.setButtonEX.bind("<Button-1>", self.drawSingleLineEvent)


    def arcPath(self):
        startPoint = self.TopWindow.LeftControlPanel.getStartEntry()
        endPoint = self.TopWindow.LeftControlPanel.getEndEntry()
        numOfPoints = self.TopWindow.LeftControlPanel.getNumOfPoints()

        #find the mid point
        midPoint = ( ((startPoint[0] + endPoint[0]) / 2), ((startPoint[1] + endPoint[1]) / 2) )
        print("midPoint: (" + str(midPoint[0]) + "," + str(midPoint[1]) + ")" )

        #change in x
        deltaX = startPoint[0] - midPoint[0]
        print("deltaX: " + str(deltaX))
        #change in y
        deltaY = startPoint[1] - midPoint[1]
        print("deltaY: " + str(deltaY))

        #angle between two points:
        theta = (math.atan2(deltaY,deltaX))
        print("theta: " + str(theta))

        #degrees per movement
        degreePerMove = (math.pi / (numOfPoints-1))
        print("degreePerMove: " + str(degreePerMove))

        #calculate radius
        radius = math.sqrt(pow(deltaX,2) + pow(deltaY,2))
        print("radius: " + str(radius))

        pathCoords = []
        i = 0
        print("Arch Path: ")
        while i < numOfPoints:
            newX = int(radius * math.cos( (i*degreePerMove) + theta ) + midPoint[0])
            newY = int(radius * math.sin( (i*degreePerMove) + theta ) + midPoint[1])
            pathCoords.append((newX,newY))
            #print("cos value: " + str(math.cos( (i+1)*degreePerMove + theta )))
            #print("sin value: " + str(math.sin( (i+1)*degreePerMove + theta )))
            #print("(" + str(newX) + "," + str(newY) + ")")
            i += 1

        return pathCoords

    def linearPath(self):
        startPoint = self.TopWindow.LeftControlPanel.getStartEntry()
        endPoint = self.TopWindow.LeftControlPanel.getEndEntry()
        numOfPoints = self.TopWindow.LeftControlPanel.getNumOfPoints()

                            #change in x              #change in y
        distance = (endPoint[0]-startPoint[0], endPoint[1]-startPoint[1])
        deltaX = float(distance[0]/(numOfPoints-1))
        #print("Change in X: ",deltaX)
        deltaY = float(distance[1]/(numOfPoints-1))
        #print("Change in Y: ",deltaY)
        pathCoords = []
        i = 0
        print("Linear Path: ")
        while i < numOfPoints:
            newX = int(startPoint[0] + i * deltaX)
            newY = int(startPoint[1] + i * deltaY)
            pathCoords.append((newX,newY))
            print("(" + str(newX) + "," + str(newY) + ")")
            i += 1 
            
        #generate an array of coordinates
        return pathCoords

    def calculatePath(self):
        movementFunc = self.TopWindow.LeftControlPanel.getFunc()
        switcher = {
            "Linear Movement": self.linearPath,
            "Arc Movement": self.arcPath
        }
        function = switcher.get(movementFunc)
        return function()

        

    def drawSingleLineEvent(self, event):
        line = self.calculatePath()

        self.TopWindow.VideoWidget.drawLineSimple(line) 
    
