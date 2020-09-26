import tkinter as tk

class LeftControlPanel(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Whole Panel
        self.panel = tk.Frame(self.parent)

        # Whole Panel -> starting Point entry
        startPoint = tk.Frame(self.panel)
        startPoint.grid(row=0, column=0)
        
        StartLabel = tk.Label(startPoint, text = "Starting Point: (x, y)")
        StartLabel.grid(row=0, column=0, columnspan=2)

        parenthCharSX1 = tk.Label(startPoint,text ="(")
        parenthCharSX1.grid(row=1, column=0)

        startXEntry = tk.Entry(startPoint)
        startXEntry.grid(row=1, column=1)

        commaCharSX = tk.Label(startPoint, text =",")
        commaCharSX.grid(row=1, column=2)

        startYEntry = tk.Entry(startPoint)
        startYEntry.grid(row=1,column=3)

        parenthCharSX2 = tk.Label(startPoint,text =")")
        parenthCharSX2.grid(row=1,column=4)

        setButtonSX = tk.Button(startPoint, text="Set", width=15)
        setButtonSX.grid(row=2, column=0, columnspan=2)
        



