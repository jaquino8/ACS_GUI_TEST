# ACS_GUI_TEST
 ACS GUI via Python with Tkinter
 Has an updated GUI and a (not fully implemented) path coordinate generator between start and end.
 
For questions: ask Emil in the Group Discord
or Email at emil.agonoy2@gmail.com

## Dependencies

tkinter (Already Included with installation of Python)
opencv-python: Opencv library for python. (Install pip install opencv-python)
PILLOW: Python Imaging Library. (Install: pip install Pillow)

### Good Websites for Python Reference:
- https://www.geeksforgeeks.org/python-programming-language/
- https://www.w3schools.com/python/

*Notable Topics* 
- Tuples
- List
- class
- Dictionaires
- Functions

## Tkinter Guide
"Tkinter is a Python binding to the Tk GUI Toolkit" - https://en.wikipedia.org/wiki/Tkinter
Tkinter comes included in standard installations of Python.
The Tkinter library allows us to build an interactable GUI. 
Refer to these links to learn more about Tkinter: 
- https://www.w3schools.in/python-tutorial/gui-programming/
- https://docs.python.org/3/library/tkinter.html
- https://www.tutorialspoint.com/python/python_gui_programming.htm

*Notable Topcis*
- Button
- Label 
- Entry
- Binding Events
- Frame
- "Tkinter how to organize project" 

# Tkinter Style Guide For This Project
Mainly to Build the GUI, and have basic interaction with the widgets
Simple tkinter project diagram example should be here

The TopWindow Class is the main controller for all other frames, which collects classes of other Tkinter widgets/Frames.
To keep different parts of the UI organized, have each component as a class
Such as LeftControlPanel and VideoFrame. 

to make things accessable, make sure that member objects are set to self. 
then those can be accessed through LeftControlPanel.WhateverTheObject was
Note, not all elements need to be self. only those that will be referenced outside of the class.
    Mainly event bindable widgets. 

for data display and aquisition. create another member function that takes in or returns data of a specific element
this will be important for binding events in the event controller

# DataEventController
Class responsible for processing data between Tkinter GUI Frames

Takes in the TopWindow Object and can reference member objects 
Certain elements are interactable and show/hold data. 
These elements need to be bound to events. 
Often times, elements in one Frame, will have data that affect another element in a different frame

Keep data processing and GUI building separate
Mean more files to go through, but all data can be collected into DataEventController
If you find that another structure is better, by all-means, change it and probide new documentation on the new system. 

Tkinter binding events in binding to desired button, referenced through TopWindow.<level2frame>....

define events as member functions to the Data Event Controller
In these events, you can call the data get or data put functions that you defined when making those specific elements that get/put data. 



