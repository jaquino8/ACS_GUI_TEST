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
         

        #starting point in relation to mid point
        actualStart = ((startPoint[0] - midPoint[0]), (startPoint[1] - midPoint[1]))
        actualEnd = ((endPoint[1] - midPoint[1]), (endPoint[1] - midPoint[1]))

        #change in x
        deltaX = actualEnd[0] - actualStart[0]
        #change in y
        deltaY = actualEnd[1] - actualStart[1]

        #angle between two points:
        theta = int(math.atan2(deltaY,deltaX))

        #degrees per movement
        degreePerMove = int(theta / numOfPoints)

        #calculate radius
        radius = abs(midPoint[0] - actualStart[0])

        #calculate arc length
        arcLength = (radius * theta)

        pathCoords = []
        i = 0
        while i < numOfPoints:
            newX = int(radius * math.cos( (i+1) * degreePerMove ) + midPoint[0])
            newY = int(radius * math.sin( (i+1) * degreePerMove ) + midPoint[1])
            pathCoords.append((newX,newY))
            i += 1

        return pathCoords

    def linearPath(self):
        startPoint = self.TopWindow.LeftControlPanel.getStartEntry()
        endPoint = self.TopWindow.LeftControlPanel.getEndEntry()
        numOfPoints = self.TopWindow.LeftControlPanel.getNumOfPoints()

                            #change in x              #change in y
        distance = (endPoint[0]-startPoint[0], endPoint[1]-startPoint[1])
        deltaX = float(distance[0]/numOfPoints)
        #print("Change in X: ",deltaX)
        deltaY = float(distance[1]/numOfPoints)
        #print("Change in Y: ",deltaY)
        pathCoords = []
        i = 0
        while i < numOfPoints:
            newX = int(startPoint[0] + i * deltaX)
            newY = int(startPoint[1] + i * deltaY)
            pathCoords.append((newX,newY))
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
    
