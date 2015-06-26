# New_Amazon_Munscher
Automates Amazon's Listing Process using UPC's
<img src="https://raw.githubusercontent.com/BiTinerary/New_Amazon_Munscher/master/Win1.png">

#Requirements

* Windows OS
or
* Python w/ Numpy and Tkinter modules. (`pip install numpy` | `pip install python-tk`)

* Selenium Plugins: <ahref='http://www.seleniumhq.org/projects/ide/'>http://www.seleniumhq.org/projects/ide/</a>

* Browser needs to open new windows in the **same** tab. This is due to Selenium not being able to communicate between tabs. This can be accomplished by changing a registry entry in Firefox:
~ Type `about:config` in the address bar
~ Search for `browser.link.open_newwindow` entry.
~ Change from default `3` to `1` in order to open new windows/links in the same tab.

<a href='http://www.ghacks.net/2009/07/03/force-firefox-to-open-links-in-same-tab/'>http://www.ghacks.net/2009/07/03/force-firefox-to-open-links-in-same-tab/</a>

# Directions

~ Run the GUI. Enter load, initials, etc... assign unique SKU number and scan item's UPC.
~ After all items have been scanned exit the program. It's best to use <kbd>Esc</kbd> or the `Exit` button.
~ Open browser that has Selenium installed on it. Open the generated `ListMe.txt` and hit play.

Additional Notes:
Use <kbd>Tab</kbd> or mouse to navigate GUI. <kbd>Enter</kbd> will continue to the next GUI window, provided all input fields have content inside them. <kbd>Esc</kbd> will exit the script at any given time. Every time <kbd>Enter</kbd> is pressed, all current information will be saved to a log file and/or listing script where applicable.

<img src="https://raw.githubusercontent.com/BiTinerary/New_Amazon_Munscher/master/VidGif.gif">