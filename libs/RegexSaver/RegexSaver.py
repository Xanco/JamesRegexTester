from tkinter import *

class RegexSaver:
	def __init__(self, passedRoot):
		self.root = passedRoot


	def SetUpLoadWindow(self):
		loadWindow = Tk()
		loadWindow.grab_set()


	def Load(self):
		self.SetUpLoadWindow()

	def SetUpResexSaver(self):
		print("RegexSaverLaunched")

		MenuBar = Menu(self.root)
		#filemenu = Menu(MenuBar, tearoff=0)
		MenuBar.add_command(label="Load", command=self.Load) # If RegexSaver.test() were called it'd have to pass self - RegexSaver.self(self) and adding () will run test immediately
		#MenuBar.add_cascade(label="File", menu=filemenu)

		self.root.config(menu=MenuBar)