import os
import sys
import Tkinter as tk
import collections
from Tkinter import IntVar

GetInputList = []

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

		LoadIDLabel = tk.Label(width=15, relief='ridge',text="Load ID:")
		LoadIDLabel.grid(row=2, column=0, padx=5, pady=5)

		LoadConditionLabel = tk.Label(width=15, text="Load Condition:")
		LoadConditionLabel.grid(row=1, column=0, padx=5, pady=5)

		BinLocationLabel = tk.Label(width=15, relief='ridge', text="Bin Location:")
		BinLocationLabel.grid(row=3, column=0, padx=5, pady=5)

		ListersInitialsLabel = tk.Label(width=15, relief='ridge', text="Lister's Initials:")
		ListersInitialsLabel.grid(row=4, column=0, padx=5, pady=5)

		LoadIDEntry = tk.Entry(width=55)
		LoadIDEntry.grid(row=2, column=1, padx=5, pady=5)
		LoadIDEntry.focus_set()

		BinLocationEntry = tk.Entry(width=55)
		BinLocationEntry.grid(row=3, column=1, padx=5, pady=5)

		ListersInitialsEntry = tk.Entry(width=55)
		ListersInitialsEntry.grid(row=4, column=1, padx=5, pady=5)

		EnterButton = tk.Button(text="Enter", width=64, command=lambda: EveryEntryHasInput())
		EnterButton.grid(row=5, column=0, padx=5, pady=5, columnspan=4)
		self.bind('<Return>', (lambda event: EveryEntryHasInput()))

		def GetStaticInputs():
			ConditionList = ["NEW","LIKENEW","VERYGOOD","GOOD"]
			
			global GetLoadID
			GetLoadID = str(LoadIDEntry.get())
			GetInputList.append(GetLoadID)

			global GetBinLocation
			GetBinLocation = str(BinLocationEntry.get())
			GetInputList.append(GetBinLocation)

			global GetListersInitials
			GetListersInitials = str(ListersInitialsEntry.get())
			GetInputList.append(GetListersInitials)

			IndexToCondition = intvar.get()
			global GetConditionIndex
			GetConditionIndex = str(ConditionList[IndexToCondition])
			GetInputList.append(GetConditionIndex)

			def GoToSecondaryGui():
				self.destroy()
				SecondaryApp()
			GoToSecondaryGui()

		def EveryEntryHasInput():
			if LoadIDEntry.get().isalnum() and BinLocationEntry.get().isalnum() and ListersInitialsEntry.get().isalnum():
				GetStaticInputs()


class SecondaryApp(tk.Tk): # Main GUI window with buttons in line.
	def __init__(self):
		tk.Tk.__init__(self)
		print GetInputList

		FullListingSKULabel = tk.Label(width=64, anchor='n', relief='ridge', text=GetLoadID + "-" + GetBinLocation + "-" + GetListersInitials + "-" + GetConditionIndex)
		FullListingSKULabel.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

		SkuLabel = tk.Label(width=15, relief='ridge', text="SKU:")
		SkuLabel.grid(row=1, column=1, padx=5, pady=5)

		UpcLabel = tk.Label(width=15, relief='ridge', text="UPC")
		UpcLabel.grid(row=2, column=1, padx=5, pady=5)

		SkuEntry = tk.Entry(width=55)
		SkuEntry.grid(row=1, column=2, padx=5, pady=5)
		SkuEntry.focus_set()

		UpcEntry = tk.Entry(width=55)
		UpcEntry.grid(row=2, column=2, padx=5, pady=5)

		EnterButtonTwo = tk.Button(text="Enter", width=31, command=lambda: EveryEntryHasDynamicInput())
		EnterButtonTwo.grid(row=4, column=1, columnspan=2, padx=(0,229), pady=5)
		self.bind('<Return>', (lambda event: EveryEntryHasDynamicInput()))

		ExitButton = tk.Button(text="Exit", width=31, command=lambda: self.destroy())
		ExitButton.grid(row=4, column=1, columnspan=2, padx=(229,0), pady=5)

		LineCanvas = tk.Canvas(height=1, width=454, bg="gray")
		LineCanvas.grid(row=3, column=1, columnspan=4, pady=13)
		
		def GetDynamicInputs():
			global GetSkuEntry
			GetSkuEntry = str(SkuEntry.get())
			GetInputList.append(GetSkuEntry)

			global GetUpcEntry
			GetUpcEntry = str(UpcEntry.get())
			GetInputList.append(GetUpcEntry)

			def RepeatUntilExit():
				self.destroy()
				SecondaryApp()
			RepeatUntilExit()

		def EveryEntryHasDynamicInput():
			if SkuEntry.get().isalnum() and UpcEntry.get().isalnum():
				GetDynamicInputs()

		self.resizable(0,0)
		center(self)
		self.title("Input Sku's and Quantity")
		self.focus_force()

		#with open('ListingLogFile.txt', 'w+') as f:
		#	f.write(str(GetInputList))
		#self.lift()

if __name__ == "__main__": # compile the main class/widgets to be displayed on screen.
	root = MainApp()
	root.resizable(0,0)
	center(root)
	root.title('Auto Amazon Lister')
	root.mainloop()