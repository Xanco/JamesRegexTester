from tkinter import *
from re import *
import PyV8
import ctypes
myappid = 'Jelmour.JSRegex.1' # Set ID for this program
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) # Set program with this ID - also allows for icon to be displayed in taskbar

JsC = PyV8.JSContext() # Initialise JavaScript runner for Python
JsC.enter() # Launch JavaScript runner
root = Tk() # Setup module for generating UI

def TestTextAgainstRegex(Regex, TestText): # Define function TestTextAgainstRegex and get parameters Regex and TestText
    JsC.eval("var jsTestText = '" + str(TestText) + "'") # JavaScript runner eval (like normal JS eval) create variable with TestText
    JsC.eval("var jsRegex = new RegExp('" + str(Regex) + "')") # Create Regex with passed Regex parameter
    Passed =  JsC.eval("jsRegex.test(jsTestText)") # Test TestText against Regex
    if Passed == True: # If regex has returned true
        PassedLable.config(text = "Passed!", fg="#00CC 00") # Set text to 'Passed!' and foreground color (text color in this instance) to green
    else: # Otherwise
        if Passed == False: # If regex is false
            PassedLable.config(text = "Failed!", fg="#FF0000") # Set text to 'Failed!' and foreground color to red
        else:
            PassedLable.config(text = "Error! " + str(Passed), fg="#0000FF") # Set text to 'Error!' followed by the returned regex value and foreground color to blue

root.minsize(550,75) # Set size of window to 550px by 75px
root.resizable(width=FALSE, height=FALSE) # Make window not resizable
root.title("JavaScript Regex Tester") # Set title to JavaScript Regex Tester
root.iconbitmap('icon.ico') # Set the window (and now taskbar) icon

MotherRegexFrame = Frame(root) # Create a frame (a container) inside of root (the window) and call it MotherRegexFrame
MotherRegexFrame.pack() # Place frame with no options

RegexLableFrame = Frame(MotherRegexFrame, width = 250, height = 28) # Create a new frame inside of MotherRegexFrame with the width of 250px and height of 28px and call it RegexLableFrame
RegexLableFrame.pack_propagate(0) # Make sure that frame size doesn't change
RegexLableFrame.pack({"side": "left"}) # Place on left side of parent - a lot like float: left in CSS

RegexLable = Label(RegexLableFrame, text="Enter your regex here: ") # Create a label (standard text label) inside of RegexLableFrame with the text "Enter your regex here: "
RegexLable.pack({"side": "bottom"}) # Place at bottom of parent frame (adds margin to top of application)

RegexFrame = Frame(MotherRegexFrame, width = 250, height = 28) # Create a frame like RegexLableFrame but call it RegexFrame
RegexFrame.pack_propagate(0) # Don't resize
RegexFrame.pack({"side": "right"}) # This time align to the right inside the parent

regexEntry = Entry(RegexFrame) # Create a entry (textbox) inside of RegexFrame
regexEntry.pack({"fill": "x", "side": "bottom"}) # Fill the parent in the X axis and align to bottom

# This part of the UI is the same as before, except with different text and variable names
MotherTestTextFrame = Frame(root)
MotherTestTextFrame.pack()

TestTextLableFrame = Frame(MotherTestTextFrame, width = 250, height = 28)
TestTextLableFrame.pack_propagate(0)
TestTextLableFrame.pack({"side": "left"})

TestTextLable = Label(TestTextLableFrame, text="Enter the text you want to test here: ")
TestTextLable.pack({"side": "bottom"})

TestTextFrame = Frame(MotherTestTextFrame, width = 250, height = 28)
TestTextFrame.pack_propagate(0)
TestTextFrame.pack({"side": "right"})

TestTextEntry = Entry(TestTextFrame)
TestTextEntry.pack({"fill": "x", "side": "bottom"})

# Adding the all important button
CheckText = Button(root, text="Test text against regex", command= lambda: TestTextAgainstRegex(regexEntry.get(), TestTextEntry.get())) # Create button with the text "Test text against regex" that onclick fired TestTextAgainstRegex and passes the value of regexEntry and TestTextEntry
CheckText.pack()

PassedLable = Label(root, text="") # Set up the label that displayed whether the regex has passes, failed or produced an error
PassedLable.pack()

mainloop() # Start the program