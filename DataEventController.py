import tkinter as tk

class DEC:
    def __init__(self, TopWindow):
        
        self.TopWindow = TopWindow

        self.bindEvents()

    def bindEvents(self):

        self.TopWindow.LeftControlPanel.setButtonSX.bind("<Button-1>", self.saveStartEvent)
        self.TopWindow.LeftControlPanel.setButtonEX.bind("<Button-1>", self.saveEndEvent)

    def saveStartEvent(self, event):
        point = self.TopWindow.LeftControlPanel.getStartEntry()

        self.TopWindow.VideoWidget.drawPoint(point[0], point[1], (0, 255, 255), 0)

    def saveEndEvent(self, event):

        points = self.TopWindow.LeftControlPanel.getEndEntry()

        self.TopWindow.VideoWidget.drawPoint(points[0], points[1], (0, 255, 0), 1)


