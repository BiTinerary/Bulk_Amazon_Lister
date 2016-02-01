## Bulk_Amazon_Lister
Automates Amazon's Listing Process using UPC's
<img src="https://raw.githubusercontent.com/BiTinerary/New_Amazon_Munscher/master/Win1.png">

##Requirements

* Windows OS<Br>
or
* Python w/ Numpy and Tkinter modules. (`pip install numpy` | `pip install python-tk`)
Numpy Standalone Installer: <a href='http://sourceforge.net/projects/numpy/files/NumPy/1.9.2/'>http://sourceforge.net/projects/numpy/files/NumPy/1.9.2/</a>

* Selenium Plugins: <ahref='http://www.seleniumhq.org/projects/ide/'>http://www.seleniumhq.org/projects/ide/</a>

* Browser needs to open new windows in the **same** tab. This is due to Selenium not being able to communicate between tabs. This can be accomplished by changing a registry entry in Firefox:<br>
~ Type `about:config` in the address bar<br>
~ Search for `browser.link.open_newwindow` entry.<br>
~ Change from default `3` to `1` in order to open new windows/links in the same tab.<br>

<a href='http://www.ghacks.net/2009/07/03/force-firefox-to-open-links-in-same-tab/'>http://www.ghacks.net/2009/07/03/force-firefox-to-open-links-in-same-tab/</a>

If you receive an "Unable to find vcvarsall.bat" while installing Numpy, Scipy or other `pip` installations. You will need to install Windows C++ Compiler for Python, available here: <a href='https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266'>https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266></a>

## License Agreement:
Attribution-NonCommercial-ShareAlike 4.0 International (For Now)<br>
<a href='http://creativecommons.org/licenses/by-nc-sa/4.0/'>http://creativecommons.org/licenses/by-nc-sa/4.0/</a>

## Directions

~ Run the GUI. Enter load, initials, etc... assign unique SKU number and scan item's UPC.<br>
~ After all items have been scanned exit the program. It's best to use <kbd>Esc</kbd> or the `Exit` button.<br>
~ Open browser that has Selenium installed on it. Open the generated `ListMe.txt` and hit play.<br>

Additional Notes:
Use <kbd>Tab</kbd> or mouse to navigate GUI. <kbd>Enter</kbd> will continue to the next GUI window, provided all input fields have content inside them. <kbd>Esc</kbd> will exit the script at any given time. Every time <kbd>Enter</kbd> is pressed, all current information will be saved to a log file and/or listing script where applicable.

<img src="https://raw.githubusercontent.com/BiTinerary/New_Amazon_Munscher/master/VidGif.gif">
