# this is a test GUI for the ACS group
# User will enter the start and endpoints they want to traverse
# GUI will calculate the distance and they create a path with the user
# given steps to reach the final point

# end goal of this gui is to take a user start and end positon
# by clicking on a webcam image and then providing the calculation
# this path is then calculated and converted to a sequence that can be
# created into a hologram to be sent to SLM to actuate laser

from tkinter import *
from PIL import ImageTk, Image
import math
import cv2

root = Tk()
root.title('Calculate distance between two points')

#generates and places labels for user input
startXLabel = Label(root,text ="Start X:")
startYLabel = Label(root,text ="Start Y:")
endXLabel = Label(root,text ="End X:")
endYLabel = Label(root,text ="End Y:")
numOfPointsLabel = Label(root,text ="How many steps: ")

startXLabel.grid(row=0,column=0)
startYLabel.grid(row=1,column=0)
endXLabel.grid(row=0,column=2)
endYLabel.grid(row=1,column=2)
numOfPointsLabel.grid(row=3,column=0)

startX = Entry(root)
startX.grid(row=0,column=1)
startY = Entry(root)
startY.grid(row=1,column=1)
endX = Entry(root)
endX.grid(row=0,column=3)
endY = Entry(root)
endY.grid(row=1,column=3)
numOfPoints = Entry(root)
numOfPoints.grid(row=3,column=1)

cap = cv2.VideoCapture(0)
app = Frame(root, bg="white")
app.grid()
lmain = Label(app)
lmain.grid()
circlePosition = None
def video_stream():
    _, frame = cap.read()

    if(circlePosition):
        cv2.circle(frame, circlePosition, 15, (0, 255, 255), -1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)

def setStart(event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN:
        global circlePosition 
        circlePosition = (x, y)
        
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', click_event)

#creates textbox to display output of path generation calculations
textBox = Text(root, height = 20,width = 80)
textBox.grid(columnspan=20)

def printPath(pathCoords):
    textBox.delete('1.0',END)
    for a,b in pathCoords:
        output = f"( {a} , {b} )\n"
        textBox.insert(END, output)
    

#takes calculated values from calDistance and starting coordinates
#and prints the coordinates to console and as labels that appear on GUI
def makePath(x1, y1, distance,numOfPoints):
    deltaX = float(distance[0]/numOfPoints)
    print("Change in X: ",deltaX)
    deltaY = float(distance[1]/numOfPoints)
    print("Change in Y: ",deltaY)
    pathCoords = [0] * int(numOfPoints + 1)
    i = 0
    while i < len(pathCoords):
        newX = x1 + i * deltaX
        newY = y1 + i * deltaY
        pathCoords[i] = (newX,newY)
        i += 1 
    printPath(pathCoords)



#finds the distance between the X and Y coordinates to use
#to calculate increment distance between points
def calDistance(x1,y1,x2,y2,numOfPoints):
    distance = ( x2-x1 , y2-y1 )
    print("Distance: ", distance)
    makePath(x1,y1,distance,numOfPoints)

#when user clicks generate path button, it begins the calculations and prints results
def myClick():
    calDistance(float(startX.get()),float(startY.get()),float(endX.get()),float(endY.get()),float(numOfPoints.get()))
    
#defines button to start calculations
myButton = Button(root, text="Get Path",command=myClick)
myButton.grid(row=0,column=10)

#loop to keep GUI open
video_stream()
root.mainloop()