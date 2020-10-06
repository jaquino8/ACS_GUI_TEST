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

        #self.TopWindow.LeftControlPanel.setButtonSX.bind("<Button-1>", self.saveEvent)
        self.TopWindow.LeftControlPanel.setButtonEX.bind("<Button-1>", self.saveEndEvent)


    

    def calculatePath(self):
        startPoint = self.TopWindow.LeftControlPanel.getStartEntry()
        endPoint = self.TopWindow.LeftControlPanel.getEndEntry()
        numOfPoints = self.TopWindow.LeftControlPanel.getNumOfPoints()
                            #change in x              #change in y
        distance = (endPoint[0]-startPoint[0], endPoint[1]-endPoint[1])
        deltaX = float(distance[0]/numOfPoints)
        #print("Change in X: ",deltaX)
        deltaY = float(distance[1]/numOfPoints)
        #print("Change in Y: ",deltaY)
        pathCoords = []
        i = 0
        while i < numOfPoints:
            newX = startPoint[0] + i * deltaX
            newY = startPoint[1] + i * deltaY
            pathCoords.append((newX,newY))
            i += 1 
            
        #generate an array of coordinates
        return pathCoords

    #combine these and just draw all points
    def saveEvent(self, event):
        points = []
        points = self.calculatePath()

        for point in points:
            self.TopWindow.VideoWidget.drawPoint(int(point[0]), int(point[1]), (0, 255, 255), 0)

    def saveEndEvent(self, event):

        points = self.TopWindow.LeftControlPanel.getEndEntry()

        self.TopWindow.VideoWidget.drawPoint(int(points[0]), int(points[1]), (0, 255, 0), 1)

    
