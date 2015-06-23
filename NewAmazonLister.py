import os
import sys
import Tkinter as tk
import collections
from Tkinter import IntVar

def center(toplevel): # Function for centering all windows upon execution.
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth() #Find width resolution
    h = toplevel.winfo_screenheight() #Find height resolution
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2 # find the middle of width resolution
    y = h/2 - size[1]/2 # find the middle of height resolution
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

class MainApp(tk.Tk): # Main GUI window with buttons in line.
	def __init__(self):
		tk.Tk.__init__(self)

		intvar = IntVar()

		NewButton = tk.Radiobutton(text="New", width=10, value=0, variable=intvar) #, command=lambda: GetInputList.append("NEW")
		NewButton.place(x=106, y=5)
		NewButton.select()

		LikeNewButton = tk.Radiobutton(text="Like New", width=10, value=1, variable=intvar) #, command=lambda: GetInputList.append("LIKENEW")
		LikeNewButton.place(x=196, y=5)

		VeryGoodButton = tk.Radiobutton(text="Very Good", width=10, value=2, variable=intvar) #, command=lambda: GetInputList.append("VERYGOOD")
		VeryGoodButton.place(x=286, y=5)

		GoodButton = tk.Radiobutton(text="Good", width=10, value=3, variable=intvar) # ,command=lambda: GetInputList.append("GOOD")
		GoodButton.place(x=376, y=5)

		###

		LoadIDLabel = tk.Label(width=15, text="Load ID:")
		LoadIDLabel.grid(row=2, column=0, padx=5, pady=5)

		LoadConditionLabel = tk.Label(width=15, text="Load Condition:")
		LoadConditionLabel.grid(row=1, column=0, padx=5, pady=5)

		BinLocationLabel = tk.Label(width=15, text="Bin Location:")
		BinLocationLabel.grid(row=3, column=0, padx=5, pady=5)

		ListersInitialsLabel = tk.Label(width=15, text="Lister's Initials:")
		ListersInitialsLabel.grid(row=4, column=0, padx=5, pady=5)

		LoadIDEntry = tk.Entry(width=55)
		LoadIDEntry.grid(row=2, column=1, padx=5, pady=5)

		BinLocationEntry = tk.Entry(width=55)
		BinLocationEntry.grid(row=3, column=1, padx=5, pady=5)

		ListersInitialsEntry = tk.Entry(width=55)
		ListersInitialsEntry.grid(row=4, column=1, padx=5, pady=5)

		EnterButton = tk.Button(text="Enter", width=60, command=lambda: GetStaticInputs())
		EnterButton.grid(row=5, column=0, padx=5, pady=5, columnspan=4)
		self.bind('<Return>', (lambda event: GetStaticInputs()))

		global GetInputList
		GetInputList = []

		def GetStaticInputs():
			ConditionList = ["NEW","LIKENEW","VERYGOOD","GOOD"]
			GetInputList.append(LoadIDEntry.get())
			#LOADID = LoadIDEntry.get()

			GetInputList.append(BinLocationEntry.get())
			BINLOCATION = BinLocationEntry.get()

			GetInputList.append(ListersInitialsEntry.get())
			#INITIALS = ListersInitialsEntry.get()

			IndexToCondition = intvar.get()
			GetInputList.append(ConditionList[IndexToCondition])
			#ITEMCONDITION = ConditionList[IndexToCondition]

			def GetDynamicInputs():
				root.destroy()
				SecondaryApp()
			GetDynamicInputs()


class SecondaryApp(tk.Tk): # Main GUI window with buttons in line.
	def __init__(self):
		tk.Tk.__init__(self)
		#print GetInputList

		#with open('ListingLogFile.txt', 'w+') as f:
		#	f.write(str(GetInputList))
		"""
		if __name__ == "__main__":
			SecondaryRoot = SecondaryApp()
			SecondaryRoot.resizable(0,0)
			center(SecondaryRoot)
			SecondaryRoot.title('Auto Amazon Lister')
		"""

		self.resizable(0,0)
		center(self)
		self.title("Input Sku's and Quantity")
		self.mainloop()

if __name__ == "__main__": # compile the main class/widgets to be displayed on screen.
	root = MainApp()
	root.resizable(0,0)
	center(root)
	root.title('Auto Amazon Lister')
	root.mainloop()