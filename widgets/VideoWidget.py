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
        global userClickStartPoint
        userClickStartPoint = None
        self.endPoint = None
        self.numOfPoints = None
        self.clickPoint = None

        global circles
        circles = []

        global minRadiusVal
        minRadiusVal = -1
        global maxRadiusVal
        maxRadiusVal = -1
        
        global userParam1
        userParam1 = 1

        global userParam2
        userParam2 = 1

        global detectionActive
        detectionActive = 0

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
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

        if (self.vid.isOpened()):
            ret, frame = self.vid.read()
            imageCopy = frame.copy()

            if (ret):
                
                if userClickStartPoint is not None:
                    cv2.circle(frame, userClickStartPoint, 5, (0, 0, 255), 4)

                if (self.points):
                        for point in self.points: 
                            cv2.circle(imageCopy, point, 5, (0, 0, 255), 1)
                            out.write(imageCopy)
                            #cv2.circle(frame, point, 5, (0, 0, 255), 1)
                            #cv2.imshow('Video', imageCopy)
                            #return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                        cv2.imshow('Output', imageCopy)

                if(detectionActive == 1):
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Incorporates a grayscale into the image
                    GaussBlur = cv2.GaussianBlur(gray, (7, 7), cv2.BORDER_DEFAULT) #Incorporates a Gaussian Blur into the image.
                    global circles
                    circles = cv2.HoughCircles(GaussBlur, cv2.HOUGH_GRADIENT, 1, 50, param1=userParam1, param2=userParam2, minRadius=minRadiusVal, maxRadius=maxRadiusVal)
                
                    if circles is not None:

                        circles = np.round(circles[0, :]).astype("int")
                        
                        for (x, y, r) in circles:
                            cv2.circle(frame, (x,y), r, (212,175,55), 4)
                            #print("x: " + str(x) + ", y: " + str(y) + ", r: " + str(r))
                    #cv2.imshow('Video', GaussBlur)
                    
                    #return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
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
        
    def activateDetection(self, active):
        global detectionActive
        detectionActive = active
    
    def drawStartPoint(self, origin):
        global userClickStartPoint
        userClickStartPoint = origin
        #self.startPoint = origin
        #print("Start Point: " + str(self.startPoint))
        print("Start Point: " + str(userClickStartPoint))
        print("drew a start point!")

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
        if(circles is None):
            return []
        return circles
    
    def setDetectSettings(self, settings):
        #print("video widget function called!")
        global minRadiusVal
        minRadiusVal = settings[0][0]
        #print(str(radiusValues[0]))
        global maxRadiusVal
        maxRadiusVal = settings[0][1]
        #print(str(radiusValues[1]))

        global userParam1
        userParam1 = settings[1][0]

        global userParam2
        userParam2 = settings[1][1]
    
    
    def __del__(self):
        if (self.vid.isOpened()):
            self.vid.release()
