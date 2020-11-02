import tkinter as tk
import cv2 as cv2
import numpy as np
import PIL.Image, PIL.ImageTk

class VideoWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        #self.LeftControlPanel = LeftControlPanel(self)
        
        # points: [ ((x, y), (R, B, G)), ..., ((x, y), (B, G, R))]

        # dictionary of lines
        # { "LineID": [List of points on the line], ..., "LineIDX" :[]}
        self.lines = dict() 
        self.points = [] 
        self.startPoint = None
        self.endPoint = None
        self.numOfPoints = None
        self.clickPoint = None
        global minRadiusVal
        minRadiusVal = -1
        global maxRadiusVal
        maxRadiusVal = -1

        
        self.video_source = 0 # determines the video feed
        self.vid = cv2.VideoCapture(self.video_source)

        #cv2.namedWindow('Video')
        #cv2.setMouseCallback('Video',self.click_event)

        if (not self.vid.isOpened):
            raise ValueError("Unable to open video source", video_source)
        
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.videoFrame = tk.Frame(self.parent)
        
        dimensionText = str(self.width) + " X " + str(self.height)

        self.dimensionDisplay = tk.Label(self.videoFrame, text=dimensionText)
        self.dimensionDisplay.grid(row=0, column=0, sticky="NW")

        self.videoCanvas = tk.Canvas(self.videoFrame, width = self.width, height = self.height)
        self.videoCanvas.grid(row=1, column=0)
        
    def get_frame(self):
        if (self.vid.isOpened()):
            ret, frame = self.vid.read()

            if (ret):
                
                """if(self.startPoint):
                    cv2.circle(frame, self.startPoint[0], 5, self.startPoint[1], -1)
                if(self.endPoint):
                    cv2.circle(frame, self.endPoint[0], 5, self.endPoint[1], -1)
                """
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                global circles
                circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.5, 200, minRadius=minRadiusVal, maxRadius=maxRadiusVal)
                
                if circles is not None:
                    

                    circles = np.round(circles[0, :]).astype("int")
                    
                    for (x, y, r) in circles:
                        cv2.circle(frame, (x,y), r, (0,255,0), 4)
                        #print("x: " + str(x) + ", y: " + str(y) + ", r: " + str(r))
                #cv2.imshow('Video', frame)
                if (self.points):
                    for point in self.points: 
                        cv2.circle(frame, point, 5, (0, 0, 255), 1)
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    def update(self):
        ret, frame = self.get_frame()

        if (ret):
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.videoCanvas.create_image(0, 0, image= self.photo, anchor = tk.NW)        

    def addLine(self, lineID, points):
        self.lines[lineID] = points

    def drawLineSimple(self, line):
        # Will add points to draw, will be static on the video feed
        self.points = line

    def drawLines(self):
        raise NotImplementedError
        
    # Color: (B, G, R)
    def drawPoint(self, x, y, color, position):
        
        if( 0 <= x <= self.width and 0 <= y <= self.height):
            if (position == 0): #starting point
                self.startPoint = ((x, y), color)
            elif (position == 1): #end point
                self.endPoint = ((x, y), color)
            else:
                self.points.append((x, y), color)

    
    def click_event(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            global clickPoint
            clickPoint = (x,y)
            #print(clickPoint)
            
            
    def getClickPoint(self):
        return clickPoint

    def getDetectedCircles(self):
        return circles
    
    def setDetectSettings(self, radiusValues):
        #print("video widget function called!")
        global minRadiusVal
        minRadiusVal = radiusValues[0]
        #print(str(radiusValues[0]))
        global maxRadiusVal
        maxRadiusVal = radiusValues[1]
        #print(str(radiusValues[1]))
    

    def __del__(self):
        if (self.vid.isOpened()):
            self.vid.release()