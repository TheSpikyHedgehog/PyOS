#############################################################################
#----
# WARNING: The files must be kept under a folder named "PyOS". The program is coded so. 
# Although if you really want to change it, you may reprogram the parts that use the folder name
# like file paths. 
###########################
# Author: TheSpikyHedgehog
#--------------------------------------------------------------
#   Copyright (C) 2023  @TheSpikyHedgehog
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#-----------------------------------------------------------------------

#Enjoy!
##############################################################################

from tkinter import * 
import tkinter.ttk as ttk
import os
from datetime import date



class Desktop:
    def __init__(self):
        # set basics
        self.root = Tk()
        self.root.iconbitmap("start.ico")
        self.root.title("PyOS Desktop GUI")
        self.root.deiconify()
        self.root.resizable(0, 0)
        self.root.geometry('1400x800')
        self.root.configure(bg="LightBlue")

        # creating the wallpaper and taskbar
        canvas = Canvas(self.root, width = 10000, height = 10000, bg="LightBlue")
        canvas.pack(fill = "both", expand = True)

        #wallpaper rectangles
        canvas.create_rectangle(1100, 400, 400, 600, fill="lightyellow")
        canvas.pack()
        canvas.create_rectangle(600, 80, 400, 400, fill="green")
        canvas.pack()
        canvas.create_rectangle(1100, 80, 600, 400, fill="orange")
        canvas.pack()
        canvas.create_polygon(1200, 100, 800, 100, 100, 30, fill="yellow")
        canvas.pack()
        canvas.create_polygon(600, 50, 400, 100, 50, 605, fill="lightgreen")
        canvas.pack()
        canvas.create_polygon(1600, 100, 1500, 50, 50, 2300, fill="pink")
        canvas.pack()
        pyos = Label(text="Py Desktop GUI", font=("Tahoma", 40), bg='Lightyellow', fg = "Green")
        pyos.place(x=560, y=450)
        # taskbar
        canvas.create_rectangle(1500,745,0,1100, fill="Black")
        canvas.pack()

        

    def datelabel(self):
        curtime = date.today()
        print(curtime)
        time = Label(text=f"{curtime}", fg="White", bg="Black", font=("Tahoma", 14))
        time.place(x=1290, y=754)

    def start_popup(self):
        #popup menu
        self.popup_menu = Menu(self.root, tearoff = 0)
        self.popup_menu.insert(itemType="separator", index=0)
        
        self.popup_menu.add_command(label = "Calulator",
                                    command = lambda: os.system("start  calulator.pyw"))
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label = "PyMusic",
                                    command = lambda: os.system("start  py_music.pyw"))
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label = "PyCode",
                                    command = lambda: os.system("start  py_code.pyw"))
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label = "PyNotes",
                                    command = lambda: os.system("start  PyNotes/PyNotes.pyw"))
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label = "Sierpinski Triangle",
                                    command = lambda: os.system("start  sierpinski_triangle.pyw"))
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label = "Yellow Window",
                                    command = lambda: new_win(color="Yellow"))
        self.popup_menu.add_separator()
        def new_win(color):
            new = Tk()
            new.title(f"{color} Window")
            new.configure(bg=color)
            new.mainloop

    def do_popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root,
                                     event.y_root)

        finally:
            self.popup_menu.grab_release()

    def run(self):
        self.start_popup()
        self.taskbar()
        self.datelabel()
        self.root.mainloop()

        # self.root.bind("<Control-q>",self.do_popup)
        
    
    def taskbar(self):
        #start button

        start_btn = Button(self.root, text= "⭘",font=("Tahoma", 15), command= lambda: self.popup_menu.tk_popup(x=80,y=640))
        start_btn.place(x=10, y=751)
        pynotes_btn = Button(self.root, text= "PyNotes", font=("Tahoma", 15), command= lambda: os.system("start PyNotes.pyw"))
        pynotes_btn.place(x=70, y=751)
        pycode = Button(self.root, text= "PyCode", font=("Tahoma", 15), command= lambda: os.system("start  py_code.pyw"))
        pycode.place(x=180, y=751)

start = Desktop()
start.run()
