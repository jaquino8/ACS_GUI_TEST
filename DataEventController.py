import tkinter as tk
import cv2 as cv2
from widgets.Controls import LeftControlPanel
from widgets.VideoWidget import VideoWidget
import math

class DEC:
    def __init__(self, TopWindow, VideoWidget):
        
        self.TopWindow = TopWindow
        self.VideoWidget = VideoWidget

        self.bindEvents()

        # dictionairy of lines
        # { "LineID": [List of points on the line], ..., "LineIDX" :[]}
        # point format: ((x, y), (B, G, R))
        self.lines = dict() 

        # pointCollections = None # should be a collection of points
        
    def bindEvents(self):

        self.TopWindow.LeftControlPanel.setButtonEX.bind("<Button-1>", self.drawSingleLineEvent)
        self.TopWindow.LeftControlPanel.setButtonDetectSettings.bind("<Button-1>",self.setDetectSettings)
        self.TopWindow.LeftControlPanel.showVideo.bind("<Button-1>", self.showVideoEvent)

        self.TopWindow.VideoWidget.bind_class("Canvas","<Button-3>",self.clickCoordinates)
        self.TopWindow.VideoWidget.bind_class("Canvas","<Button-1>",self.drawStartPoint)
        #self.TopWindow.VideoWidget.bind_class("Canvas","<Enter>",self.updateCirCount)
        #self.TopWindow.VideoWidget.bind_class("Canvas","<Leave>",self.updateCirCount)
        

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
        print("Arc Path: ")
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

    def drawStartPoint(self, event):
        startPoint = (event.x,event.y)
        self.VideoWidget.drawStartPoint(startPoint)
        self.TopWindow.LeftControlPanel.setStartPoint(startPoint)

    def clickCoordinates(self,event):
        clickPoint = (event.x,event.y)
        #print(clickPoint)
        self.TopWindow.LeftControlPanel.setROIPoint(clickPoint)
        

    def drawSingleLineEvent(self, event):
        line = self.calculatePath()

        self.TopWindow.VideoWidget.drawLineSimple(line) 

    def setDetectSettings(self, event):
        print("this function was called")
        self.VideoWidget.setDetectSettings(self.TopWindow.LeftControlPanel.getDetectSettings())
     
        
    def updateCirCount(self):
        detectedCircles = self.VideoWidget.getDetectedCircles()
        self.TopWindow.LeftControlPanel.detectedCirCount(len(detectedCircles))

    def showVideoEvent(self, event):
        # Create a VideoCapture object and read from input file 
        cap = cv2.VideoCapture('output.avi') 
   
        # Check if camera opened successfully 
        if (cap.isOpened()== False):  
            print("Error opening video  file") 
   
        # Read until video is completed 
        while(cap.isOpened()): 
      
        # Capture frame-by-frame 
            ret, frame = cap.read() 
            if ret == True: 
   
            # Display the resulting frame 
                cv2.imshow('Frame', frame) 
   
            # Press Q on keyboard to  exit 
                if cv2.waitKey(25) & 0xFF == ord('q'): 
                    break
   
            # Break the loop 
            else:  
                break
   
