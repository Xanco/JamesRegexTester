from Tkinter import *

class RegexSaver:
	def __init__(self, passedRoot, mother):
		self.root = passedRoot
		self.mainUI = mother


	def SetUpLoadWindow(self):
		loadWindow = Tk()
		
		# Setup load options listbox
		LoadOptionsFrame = Frame(loadWindow)
		LoadOptionsFrame.pack({"fill": "x"})
		LoadOptionScrollBar = Scrollbar(LoadOptionsFrame, orient=VERTICAL)
		LoadOptions = Listbox(LoadOptionsFrame, yscrollcommand=LoadOptionScrollBar.set)
		LoadOptionScrollBar.config(command=LoadOptions.yview)
		LoadOptionScrollBar.pack({"side":"right", "fill": "y"})
		LoadOptions.pack({"fill": "x"})
		for item in ["1","2","3","1","2","3","1","2","3","1","2","3","1","2","3","1","2","3","1","2","3","1","2","3","1","2","3","1","2","3","1","2","3","1","2","3","1","2","3"]:
			LoadOptions.insert(END, item)
		
		# Setup load button
		#LoadButton

	def Load(self):
		self.SetUpLoadWindow()

	def SetUpResexSaver(self):
		print("RegexSaverLaunched")

		MenuBar = Menu(self.root)
		MenuBar.add_command(label="Load", command=self.Load) # If RegexSaver.test() were called it'd have to pass self - RegexSaver.self(self) and adding () will run test immediately

		self.root.config(menu=MenuBar)