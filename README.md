# <p style="text-align: center;"> PyOS Desktop GUI </p>
<p align="center"> 
          <img 
               src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue&color=4f4f4f" 
               Title="100% Python"  
          />
          <img 
               src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=ffffff&color=blue" 
               Title="Software Used: VSCode" 
          />
     </p>


>Note: The file extensions are .pyw because they are used to make console-less windows.  The files are still editable and if you can't, you can just turn them into regular Python files (.py).  Just don't forget to turn them back in Python Windowed (.pyw) after you are done!
>
>If you encounter any issues, please please create an issue and I will try to fix it.  Without your feedback, I can't improve!
# Features:
- A working notepad-like-software (PyNotes) that you can save to your real computer's hard drive.
- A working code editor that can make and edit files to your real computer's hard drive.
- A working music loader/player.
- A calulator
- A customizable Sierpinski Triangle model.
- And with more coming in the future!
# Installation:
## From Source Code:

> **WARNING:** some programs in this project do *NOT* work with Linux or MacOS.  While this may be changed in the future, please take note that PyCode and PyNotes do not work on Linux. This is because they both make a directory under "C:\\" (Linux's filesystem is different from Windows).  Despite everything, it is not very important. You may remove/edit the parts requiring the directory to fit your machine's needs.
>
> *Tip: You can use software like VirtualBox or VMware to load in a windows virtual machine and run the program on there.*


Download the code and unzip it using software like 7-Zip or winRAR.
Most modules that this project uses are included in Python's standard utility modules so you shouldn't have to install a lot but just to be sure, please take a look at this list.

- pygame (mixer) 
- os (file I/O; ex. `os.mkdir("C:/PyCode")`)
- tkinter (GUI work)
- datetime (Current date)
- turtle (Graphics for the sierpinski triangle)
- ctypes
- re

How to install pygame: 
- Open up your terminal
- Type in the following command: `pip install pygame`
- Wait for it to finish and you're done!
> *Note: if `pip install pygame` doesn't work for you, try using the command `pip3 install pygame` or `python -m pip install pygame`(assuming you have python 3).  Another reliable but harder method is to download the zip or tar file from [pygame's PyPi](https://pypi.org/project/pygame/) and manually install the module.*

## Command Line (source):
#### On Linux...
You could use wget or Git (preferred) like so:

`git clone <url>`

#### On Windows...
You could install 3rd party software like [eternallybored.org's Port of GNU Wget](https://eternallybored.org/misc/wget/).

#### On MacOS (OS X)...
You could use Git: 

`git clone <url>`

> ***Important Note***: The above methods do **NOT** install the required dependencies! Please take a look at the list above.
# Licence:

Author: TheSpikyHedgehog

Copyright (C) 2023  @TheSpikyHedgehog

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


# Credits:
- Author: TheSpikyHedgehog

---
<p style="text-align: center;"> Welcome to the end of the file</p>

