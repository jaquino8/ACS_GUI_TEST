import tkinter as tk

class LeftControlPanel(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

    
        # Whole Panel
        self.panel = tk.Frame(self.parent)

        controlTopPadding = tk.Frame(self.panel)
        controlTopPadding.grid(row=0,column=0,pady=40)

        # Whole Panel -> starting Point entry
        startPoint = tk.Frame(self.panel)
        startPoint.grid(row=1, column=0,pady = 5)
        

        StartLabel = tk.Label(startPoint, text = "Start: ")
        StartLabel.grid(row=0, column=0)

        self.StartTextBox = tk.Text(startPoint, state=tk.DISABLED, height = 1,width = 12)
        self.StartTextBox.grid(row=0,column=1)

        #parenthCharSX1 = tk.Label(startPoint,text ="(")
        #parenthCharSX1.grid(row=0, column=1)

        #self.startXEntry = tk.Entry(startPoint,width=5)
        #self.startXEntry.grid(row=0, column=2)

        #commaCharSX = tk.Label(startPoint, text =",")
        #commaCharSX.grid(row=0, column=3)

        #self.startYEntry = tk.Entry(startPoint,width=5)
        #self.startYEntry.grid(row=0,column=4)

        #parenthCharSX2 = tk.Label(startPoint,text =")")
        #parenthCharSX2.grid(row=0,column=5)

        # Endpoint / ROI
        endPoint = tk.Frame(self.panel)
        endPoint.grid(row=2, column=0,pady = 5)

        endLabel = tk.Label(endPoint, text = "Ending Point: (x, y)")
        endLabel.grid(row=0, column=0, columnspan=2)

        self.ROIPointInfo = tk.Label(endPoint, text = "ROI: ")
        self.ROIPointInfo.grid(row=0,column=0)
        self.ROItextBox = tk.Text(endPoint, state=tk.DISABLED, height = 1,width = 12)
        self.ROItextBox.grid(row=0,column=1)
    

        # Number of Points
        numPoints = tk.Frame(self.panel)
        numPoints.grid(row=3, column=0,pady=10)

        numPointsLabel = tk.Label(numPoints, text = "How Many Points?")
        numPointsLabel.grid(row=0,columnspan=3)

        self.numOfPointsEntry = tk.Entry(numPoints, width=10)
        self.numOfPointsEntry.grid(row=1, column=1)

        selectFuncLabel = tk.Label(numPoints, text ="Which Movement Function?")
        selectFuncLabel.grid(row=2,columnspan=3)
        
        self.listbox = tk.Listbox(numPoints,height=2,width=18,selectmode="SINGLE")
        self.listbox.grid(row=3,columnspan=5)
        self.listbox.insert(1, "Linear Movement")
        self.listbox.insert(2, "Arc Movement")
        #self.listbox.insert(2, "Arc Movement by Radius")


        #press button to get coordinates and then calculate the path
        self.setButtonEX = tk.Button(numPoints, text="Set", width=15)
        self.setButtonEX.grid(row=4, column=0, columnspan=3)

        #settings to change circle detect settings:
        cirDetectSettings = tk.Frame(self.panel)
        cirDetectSettings.grid(row=5,column=0)

        minRadiusLabel = tk.Label(cirDetectSettings, text= "Min Radius:")
        minRadiusLabel.grid(row=0,column=0)

        self.minRadiusEntry = tk.Entry(cirDetectSettings, width=10)
        self.minRadiusEntry.insert(0, "-1")
        self.minRadiusEntry.grid(row=0,column=1)

        minRadiusLabel = tk.Label(cirDetectSettings, text= "Max Radius:")
        minRadiusLabel.grid(row=1,column=0)
        
        self.maxRadiusEntry = tk.Entry(cirDetectSettings, width=10)
        self.maxRadiusEntry.insert(0, "-1")
        self.maxRadiusEntry.grid(row=1,column=1)

        param1Label = tk.Label(cirDetectSettings, text= "Param1:")
        param1Label.grid(row=2,column=0)
        
        self.param1Entry = tk.Entry(cirDetectSettings, width=10)
        self.param1Entry.insert(0, "1")
        self.param1Entry.grid(row=2,column=1)

        param2Label = tk.Label(cirDetectSettings, text= "Param2:")
        param2Label.grid(row=3,column=0)
        
        self.param2Entry = tk.Entry(cirDetectSettings, width=10, text="1")
        self.param2Entry.insert(0, "1")
        self.param2Entry.grid(row=3,column=1)

        self.detectedCircles = tk.Label(cirDetectSettings, text = "Circles Detected: ")
        self.detectedCircles.grid(row=4,column=0)
        self.detectedCirclestextBox = tk.Text(cirDetectSettings, state=tk.DISABLED, height = 1,width = 3)
        self.detectedCirclestextBox.grid(row=4,column=1)

        self.setButtonDetectSettings = tk.Button(cirDetectSettings, text="Set", width=15)
        self.setButtonDetectSettings.grid(row=5,column=0,columnspan=2)

    def setStartPoint(self,point):
        self.StartTextBox.config(state=tk.NORMAL)
        self.StartTextBox.delete('1.0',tk.END)
        global startPoint 
        startPoint = point
        output = "(" + str(point[0]) + "," + str(point[1]) + ")"
        #print(output)
        self.StartTextBox.insert(tk.END,output)
        self.StartTextBox.config(state=tk.DISABLED)

    def setROIPoint(self,point):
        self.ROItextBox.config(state=tk.NORMAL)
        self.ROItextBox.delete('1.0',tk.END)
        global ROIPoint 
        ROIPoint = point
        output = "(" + str(point[0]) + "," + str(point[1]) + ")"
        #print(output)
        self.ROItextBox.insert(tk.END,output)
        self.ROItextBox.config(state=tk.DISABLED)

    def getStartEntry(self):
        x = startPoint[0]
        y = startPoint[1]

        return (int(x), int(y))
    
    def getEndEntry(self):
        x = ROIPoint[0]
        y = ROIPoint[1]
        #x = self.endXEntry.get()
        #y = self.endYEntry.get()
        
        return (int(x), int(y))

    def getNumOfPoints(self):
        numPoints = self.numOfPointsEntry.get()
        return int(numPoints)

    def getFunc(self):
        index = int(self.listbox.curselection()[0])
        function = str(self.listbox.get(index))
        return function

        
    def getDetectSettings(self):
        minRadius = self.minRadiusEntry.get()
        maxRadius = self.maxRadiusEntry.get()
        radiusValues = (int(minRadius), int(maxRadius))

        userParam1 = self.param1Entry.get()
        userParam2 = self.param2Entry.get()
        userParamValues = (int(userParam1),int(userParam2))

        return (radiusValues, userParamValues)

    def detectedCirCount(self, count):
        self.detectedCirclestextBox.config(state=tk.NORMAL)
        self.detectedCirclestextBox.delete('1.0',tk.END)
        output = str(count)
       
        #print(output)
        self.detectedCirclestextBox.insert(tk.END,output)
        self.detectedCirclestextBox.config(state=tk.DISABLED)