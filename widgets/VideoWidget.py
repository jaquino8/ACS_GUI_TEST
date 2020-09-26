import tkinter as tk
import cv2 as cv2
import PIL.Image, PIL.ImageTk

class VideoWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.video_source = 0 # determines the video feed
        self.vid = cv2.VideoCapture(self.video_source)

        if (not self.vid.isOpened):
            raise ValueError("Unable to open video source", video_source)
        
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.videoFrame = tk.Frame(self.parent)
        
        self.videoCanvas = tk.Canvas(self.videoFrame, width = self.width, height = self.height)
        self.videoCanvas.grid(row=0, column=0)

        self.startPoint = None
        
    def get_frame(self):
        if (self.vid.isOpened()):
            ret, frame = self.vid.read()

            if (ret):
                if (self.startPoint):
                    cv2.circle(frame, self.startPoint, 5, (0, 255, 255), -1)
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

    def drawPoint(self, x, y):
        print(x, " ", y)
        self.startPoint = (x, y)

    def __del__(self):
        if (self.vid.isOpened()):
            self.vid.release()