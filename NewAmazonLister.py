import Tkinter as tk
from Tkinter import IntVar
import numpy as np

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
		self.bind('<Key-Escape>', (lambda event: self.destroy()))

		def GetStaticInputs():
			ConditionList = ["NEW","LIKENEW","VERYGOOD","GOOD"]

			global GetLoadID
			global GetBinLocation
			global GetListersInitials
			global GetConditionIndex

			GetLoadID = str(LoadIDEntry.get())

			GetBinLocation = str(BinLocationEntry.get())

			GetListersInitials = str(ListersInitialsEntry.get())

			IndexToCondition = intvar.get()
			GetConditionIndex = str(ConditionList[IndexToCondition])

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
		#print GetInputList1

		try:
			FullListingSKULabel = tk.Label(width=31, anchor='n', relief='ridge', text=GetLoadID + "-" + GetBinLocation + "-" + GetListersInitials + "-" + GetSkuEntry)
			FullListingSKULabel.grid(row=0, column=1, padx=(0,229), pady=5, columnspan=2)
		
		except NameError:
			FullListingSKULabel = tk.Label(width=31, anchor='n', relief='ridge', text=GetLoadID + "-" + GetBinLocation + "-" + GetListersInitials)
			FullListingSKULabel.grid(row=0, column=1, padx=(0,229), pady=5, columnspan=2)

		ConditionLabel = tk.Label(width=31, anchor='n', relief='ridge', text="Condition: " + GetConditionIndex)
		ConditionLabel.grid(row=0, column=1, padx=(229,0), pady=5, columnspan=2)

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

		ExitButton = tk.Button(text="Exit and Create Listings", width=31, command=lambda: GenerateListings())
		ExitButton.grid(row=4, column=1, columnspan=2, padx=(229,0), pady=5)
		self.bind('<Key-Escape>', (lambda event: GenerateListings()))

		LineCanvas = tk.Canvas(height=1, width=454, bg="gray")
		LineCanvas.grid(row=3, column=1, columnspan=4, pady=13)
		
		def CreateFullSKU():

			GetInputList.append(GetLoadID)
			GetInputList.append(GetBinLocation)
			GetInputList.append(GetListersInitials)
			GetInputList.append(GetConditionIndex)

			global GetSkuEntry
			GetSkuEntry = str(SkuEntry.get())
			GetInputList.append(GetSkuEntry)

			global GetUpcEntry
			GetUpcEntry = str(UpcEntry.get())
			GetInputList.append(GetUpcEntry)

			def RepeatUntilExit():
				self.destroy()
				global ConvertList2DArray
				ConvertList2DArray = np.reshape(GetInputList, (-1, 6))
				print ConvertList2DArray
				with open('ListingLogFile.txt', 'w+') as LogFile:
					LogFile.write(str(ConvertList2DArray))
				SecondaryApp()
			RepeatUntilExit()

		def EveryEntryHasDynamicInput():
			if SkuEntry.get().isalnum() and UpcEntry.get().isalnum():
				CreateFullSKU()

		def GenerateListings():
			self.destroy()
			SeleniumHeader = str('<?xml version="1.0" encoding="UTF-8"?>'"\n"
			'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'"\n"
			'<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">'"\n"
			'<head profile="http://selenium-ide.openqa.org/profiles/test-case">'"\n"
			'<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />'"\n"
			'<link rel="selenium.base" href="http://www.amazon.com/" />'"\n"
			'<title>New Test</title>'"\n"
			'</head>'"\n"
			'<body>'"\n"
			'<table cellpadding="1" cellspacing="1" border="1">'"\n"
			'<thead>'"\n"
			'<tr><td rowspan="1" colspan="3">New Test</td></tr>'"\n"
			'</thead><tbody>'"\n"
			'<tr>'"\n"
			'	<td>store</td>'"\n"
			'	<td>New in original packaging. Factory Sealed.</td>'"\n"
			'	<td>NEW</td>'"\n"
			'</tr>'"\n"
			'<tr>'"\n"
			'	<td>store</td>'"\n"
			'	<td>Item is in excellent cosmetic condition and shows no signs of use. Includes retail packaging.</td>'"\n"
			'	<td>LIKENEW</td>'"\n"
			'</tr>'"\n"
			'<tr>'"\n"
			'	<td>store</td>'"\n"
			'	<td>Item is in excellent working condition. Show minimal signs of use with light scratches. Includes original accessories and some retail packaging.</td>'"\n"
			'	<td>VERY</td>'"\n"
			'</tr>'"\n"
			'<tr>'"\n"
			'	<td>store</td>'"\n"
			'	<td>Item is in excellent working order. Shows signs of use with scratches or scuffs. Includes original retail accessories.</td>'"\n"
			'	<td>GOOD</td>'"\n"
			'</tr>')

			SeleniumBodyRepeated = str('<tr>'"\n"
			'	<td>open</td>'"\n"
			'	<td>https://sellercentral.amazon.com/gp/ezdpc-gui/start.html/ref=ag_addlisting_dnav_xx_</td>'"\n"
			'	<td></td>'"\n"
			'</tr>'"\n"
			'<tr>'"\n"
			'	<td>type</td>'"\n"
			'	<td>id=product-search</td>'"\n"
			'	<td>ITEMIZEDUPC</td>'"\n"
			'</tr>'"\n"
			'<tr>'"\n"
			'	<td>clickAndWait</td>'"\n"
			'	<td>css=input.a-button-input</td>'"\n"
			'	<td></td>'"\n"
			'</tr>'"\n"
			'<tr>'"\n"
			'	<td>waitForTextPresent</td>'"\n"
			'	<td>Amazon Product Summary</td>'"\n"
			'	<td></td>'"\n"
			'</tr>'"\n"
			'<tr>'"\n"
			'	<td>type</td>'"\n"
			'	<td>id=offering_sku</td>'"\n"
			'	<td>SKUSTRUCTURE</td>'"\n"
			'</tr>'"\n"
			'<tr>'"\n"
			'	<td>select</td>'"\n"
			'	<td>id=offering_condition</td>'"\n"
			'	<td>LOADCONDITION</td>'"\n"
			'</tr>'"\n"
			'<tr>'"\n"
			'	<td>type</td>'"\n"
			'	<td>id=offering_condition_note</td>'"\n"
			'	<td>CONDISHNOTES</td>'"\n"
			'</tr>'"\n"
			'<tr>'"\n"
			'	<td>type</td>'"\n"
			'	<td>id=Offer_Inventory_Quantity</td>'"\n"
			'	<td>QTY</td>'"\n"
			'</tr>'"\n"
			'<tr>'"\n"
			'	<td>waitForTextPresent</td>'"\n"
			'	<td>Congratulations! Your product is now listed for sale on Amazon.</td>'"\n"
			'	<td></td>'"\n"
			'</tr>'"\n"
			'<tr>'"\n"
			'	<td>waitForTextPresent</td>'"\n"
			'	<td>Congratulations! Your product is now listed for sale on Amazon.</td>'"\n"
			'	<td></td>'"\n"
			'</tr>')

			SeleniumFooter = str('</tbody></table>'"\n"
			'</body>'"\n"
			'</html>')

			ListingInfo = ConvertList2DArray
			CompleteSKU = str(GetLoadID + "-" + GetBinLocation + "-" + GetListersInitials + "-" + GetSkuEntry)

			FinalHTML = ""
			FinalHTML += SeleniumHeader

			for Line in ListingInfo:
				LOADID = Line[0]
				BINLOC = Line[1]
				INITIALS = Line[2]
				LOADCONDITION = Line[3]
				ITEMIZEDSKU = Line[4]
				ITEMIZEDUPC = Line[5]
				FinalHTML += str(SeleniumBodyRepeated.replace('ITEMIZEDUPC', ITEMIZEDUPC).replace('SKUSTRUCTURE', CompleteSKU).replace('LOADCONDITION', LOADCONDITION))

			FinalHTML += SeleniumFooter

			with open('ListMe!.txt', 'w+') as ListingOutputFile:
				ListingOutputFile.write(FinalHTML)

		self.resizable(0,0)
		center(self)
		self.title("Input Sku's and Quantity")
		self.focus_force()

if __name__ == "__main__": # compile the main class/widgets to be displayed on screen.
	root = MainApp()
	root.resizable(0,0)
	center(root)
	root.title('Auto Amazon Lister')
	root.mainloop()