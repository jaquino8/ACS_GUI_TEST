import tkinter as tk
import cv2 as cv2
import PIL.Image, PIL.ImageTk

class VideoWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        # points: [ ((x, y), (R, B, G)), ..., ((x, y), (B, G, R))]

        # dictionary of lines
        # { "LineID": [List of points on the line], ..., "LineIDX" :[]}
        self.lines = dict() 
        self.points = [] 
        self.startPoint = None
        self.endPoint = None
        self.numOfPoints = None
        
        self.video_source = 0 # determines the video feed
        self.vid = cv2.VideoCapture(self.video_source)

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

    def __del__(self):
        if (self.vid.isOpened()):
            self.vid.release()