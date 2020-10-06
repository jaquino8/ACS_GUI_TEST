import tkinter as tk

class DEC:
    def __init__(self, TopWindow):
        
        self.TopWindow = TopWindow

        self.bindEvents()

        # dictionairy of lines
        # { "LineID": [List of points on the line], ..., "LineIDX" :[]}
        # point format: ((x, y), (B, G, R))
        self.lines = dict() 

        #UNUSED -- pointCollections = None # should be a collection of points

    def bindEvents(self):

        self.TopWindow.LeftControlPanel.setButtonEX.bind("<Button-1>", self.calculatePath)
        #REMOVED -- self.TopWindow.LeftControlPanel.setButtonSX.bind("<Btton-1>", self.saveEvent)

    def calculatePath(self, event):
        startPoint = self.TopWindow.LeftControlPanel.getStartEntry()
        endPoint = self.TopWindow.LeftControlPanel.getEndEntry()
                            #change in x              #change in y
        distance = (endPoint[0]-startPoint[0], endPoint[1]-startPoint[1])
        numOfPoints = 5
        deltaX = (distance[0]/numOfPoints)
        #print("Change in X: ",deltaX)
        deltaY = (distance[1]/numOfPoints)
        #print("Change in Y: ",deltaY)
        pathCoords = [0] * int(numOfPoints + 1)
        i = 0
        while i < len(pathCoords):
            newX = startPoint[0] + i * deltaX
            newY = startPoint[1] + i * deltaY
            pathCoords[i] = (newX,newY)
            self.TopWindow.VideoWidget.drawPoint(int(newX), int(newY), (0, 255, 255), 0)
            i += 1 
            
        
        #generate an array of coordinates

    #combine these and just draw all points
    def saveEvents(self, event):
        point = self.TopWindow.LeftControlPanel.getStartEntry()

        self.TopWindow.VideoWidget.drawPoint(point[0], point[1], (0, 255, 255), 0)

        points = self.TopWindow.LeftControlPanel.getEndEntry()

        self.TopWindow.VideoWidget.drawPoint(points[0], points[1], (0, 255, 0), 1)

    #REMOVED -- def saveEndEvent(self, event):



    
