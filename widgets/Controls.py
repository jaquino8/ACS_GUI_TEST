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

        self.startXEntry = tk.Entry(startPoint)
        self.startXEntry.grid(row=1, column=1)

        commaCharSX = tk.Label(startPoint, text =",")
        commaCharSX.grid(row=1, column=2)

        self.startYEntry = tk.Entry(startPoint)
        self.startYEntry.grid(row=1,column=3)

        parenthCharSX2 = tk.Label(startPoint,text =")")
        parenthCharSX2.grid(row=1,column=4)

        # Endpoint 
        endPoint = tk.Frame(self.panel)
        endPoint.grid(row=1, column=0)

        endLabel = tk.Label(endPoint, text = "Ending Point: (x, y)")
        endLabel.grid(row=0, column=0, columnspan=2)

        parenthCharEX1 = tk.Label(endPoint,text ="(")
        parenthCharEX1.grid(row=1, column=0)

        self.endXEntry = tk.Entry(endPoint)
        self.endXEntry.grid(row=1, column=1)

        commaCharEX = tk.Label(endPoint, text =",")
        commaCharEX.grid(row=1, column=2)

        self.endYEntry = tk.Entry(endPoint)
        self.endYEntry.grid(row=1,column=3)

        parenthCharEX2 = tk.Label(endPoint,text =")")
        parenthCharEX2.grid(row=1,column=4)

        # Number of Points
        numPoints = tk.Frame(self.panel)
        numPoints.grid(row=4, column=0)

        numPointsLabel = tk.Label(numPoints, text = "How Many Points?")
        numPointsLabel.grid(row=0,columnspan=3)

        self.numOfPointsEntry = tk.Entry(numPoints)
        self.numOfPointsEntry.grid(row=1, column=1)

        selectFuncLabel = tk.Label(numPoints, text ="Which Movement Function?")
        selectFuncLabel.grid(row=2,columnspan=3)
        
        self.listbox = tk.Listbox(numPoints,height=2,selectmode="SINGLE")
        self.listbox.grid(row=3,columnspan=3)
        self.listbox.insert(1, "Linear Movement")
        self.listbox.insert(2, "Arc Movement")


        #press button to get coordinates and then calculate the path
        self.setButtonEX = tk.Button(numPoints, text="Set", width=15)
        self.setButtonEX.grid(row=4, column=0, columnspan=3)




    def getStartEntry(self):

        x = self.startXEntry.get()
        y = self.startYEntry.get()

        return (int(x), int(y))
    
    def getEndEntry(self):

        x = self.endXEntry.get()
        y = self.endYEntry.get()
        
        return (int(x), int(y))

    def getNumOfPoints(self):
        numPoints = self.numOfPointsEntry.get()
        return int(numPoints)

    def getFunc(self):
        index = int(self.listbox.curselection()[0])
        function = str(self.listbox.get(index))
        return function