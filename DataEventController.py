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

        self.TopWindow.LeftControlPanel.setButtonSX.bind("<Button-1>", self.saveEvents)
        #self.TopWindow.LeftControlPanel.setButtonEX.bind("<Btton-1>", self.saveEndEvent)

    def calculatePath(self, event){
        startPoint = self.TopWindow.LeftControlPanel.getStartEntry()
        endPoint = self.TopWindow.LeftControlPanel.getEndEntry()
                            #change in x              #change in y
        distance = (endPoint[0]-startPoint[0], endPoint[1]-endPoint[1])
        deltaX = float(distance[0]/numOfPoints)
        #print("Change in X: ",deltaX)
        deltaY = float(distance[1]/numOfPoints)
        #print("Change in Y: ",deltaY)
        pathCoords = [0] * int(numOfPoints + 1)
        i = 0
        while i < len(pathCoords):
            newX = x1 + i * deltaX
            newY = y1 + i * deltaY
            pathCoords[i] = (newX,newY)
            i += 1 
            }
        #generate an array of coordinates
    }

    #combine these and just draw all points
    def saveEvent(self, event):
        point = self.TopWindow.LeftControlPanel.getStartEntry()

        self.TopWindow.VideoWidget.drawPoint(points[0], points[1] (0, 255, 255), 0)

    def saveEndEvent(self, event):

        points = self.TopWindow.LeftControlPanel.getEndEntry()

        self.TopWindow.VideoWidget.drawPoint(points[0], points[1], (0, 255, 0), 1)

    
