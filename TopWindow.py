import tkinter as tk
from widgets.Controls import LeftControlPanel
from widgets.VideoWidget import VideoWidget
from DataEventController import DEC

class TopWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("WIP SLM CONTROL PANEL")

        self.LeftControlPanel = LeftControlPanel(self)
        self.VideoWidget = VideoWidget(self)

        self.LeftControlPanel.panel.grid(row=0, column=0, stick="NW")
        self.VideoWidget.videoFrame.grid(row=0, column=1)

        self.update()

    def update(self):
        self.VideoWidget.update()
        msDelay = 15
        self.parent.after(msDelay, self.update)

    
if __name__ == "__main__":
    root = tk.Tk()
    TW = TopWindow(root)
    TW.pack(side="top", fill="both", expand=True)

    DEC = DEC(TW)

    root.mainloop()