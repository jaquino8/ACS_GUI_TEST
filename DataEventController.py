import tkinter as tk

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

        self.TopWindow.LeftControlPanel.buttonDrawButton.bind("<Button-1>", self.drawLineEvent)

    def calculatePath(self):
        numOfPoints = 10 # todo: get number of points from an tk.entry box

        startPoint = self.TopWindow.LeftControlPanel.getStartEntry()
        endPoint = self.TopWindow.LeftControlPanel.getEndEntry()
                            #change in x              #change in y
        distance = (endPoint[0]-startPoint[0], endPoint[1]-startPoint[1])
        deltaX = float(distance[0]/numOfPoints)
        #print("Change in X: ",deltaX)
        deltaY = float(distance[1]/numOfPoints)
        #print("Change in Y: ",deltaY)
        pathCoords =[]
        i = 0
        while i < numOfPoints:
            newX = int(startPoint[0] + i * deltaX)
            newY = int(startPoint[1] + i * deltaY)
            pathCoords.append((newX, newY))
            i += 1 

        #generate an array of coordinates
        return pathCoords

    def drawLineEvent(self, event):
        line = self.calculatePath()

        self.TopWindow.VideoWidget.drawLineSimple(line)
    
