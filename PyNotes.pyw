#importing required packages and libraries

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText
import os
root = Tk()
root.title('PyNotes')
root.resizable(0, 0)
#Note: this feature only works on windows.
try:
    os.mkdir("./PyNotes")
except FileExistsError:
    print("User already has the dirctory.")

notepad = ScrolledText(root, width = 90, height = 40)
fileName = ' ' #nooo filename


def cmdNew():     
    global fileName
    if len(notepad.get('1.0', END+'-1c'))>0:
        if messagebox.askyesno("PyNotes", "Do you want to save changes?"):
            cmdSave()
        else:
            notepad.delete(0.0, END)
    root.title("PyNotes")

def cmdOpen():     
    fd = filedialog.askopenfile(parent = root, mode = 'r') #parent root open file in read
    t = fd.read()     
    notepad.delete(0.0, END)
    notepad.insert(0.0, t)
    
def cmdSave():     
    fd = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', initialdir="./PyNotes")
    if fd!= None:
        data = notepad.get('1.0', END)
    try:
        fd.write(data)
    except:
        messagebox.showerror(title="Error", message = "Not able to save file!")
     
# def cmdSaveAs():     #file menu Save As option
#     fd = filedialog.asksaveasfile(mode='w', defaultextension = '.txt')
#     t = notepad.get(0.0, END)     #t stands for the text gotten from notepad
#     try:
#         fd.write(t.rstrip())
#     except:
#         messagebox.showerror(title="Error", message = "Not able to save file!")

def cmdExit():     
    if messagebox.askyesno("PyNotes", "Are you sure you want to exit?"):
        root.destroy()

def cmdCut():     
    notepad.event_generate("<<Cut>>")

def cmdCopy():     
    notepad.event_generate("<<Copy>>")  # << is events

def cmdPaste():     
    notepad.event_generate("<<Paste>>")

def cmdClear():     
    notepad.event_generate("<<Clear>>")
       
def cmdFind():     
    notepad.tag_remove("Found",'1.0', END)
    find = simpledialog.askstring("Find", "Find what:")
    if find:
        idx = '1.0'     
    while 1:
        idx = notepad.search(find, idx, nocase = 1, stopindex = END)
        if not idx:
            break
        lastidx = '%s+%dc' %(idx, len(find))
        notepad.tag_add('Found', idx, lastidx)
        idx = lastidx
    notepad.tag_config('Found', foreground = 'white', background = 'blue')
    notepad.bind("<1>", click)

def click(event): #click = do smth

    notepad.tag_config('Found',background='white',foreground='black')

def cmdSelectAll():    
    notepad.event_generate("<<SelectAll>>") #turns out << is like events and stuff


def cmdAbout():     #help menu About option
    label = messagebox.showinfo("About PyNotes", "PyNotes is notepad but coded in python.")

    #notepad menu items
notepadMenu = Menu(root)
root.configure(menu=notepadMenu)

#file menu
fileMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='File', menu = fileMenu)

#adding options in file menu
fileMenu.add_command(label='New', command = cmdNew)
fileMenu.add_command(label='Open...', command = cmdOpen)
fileMenu.add_command(label='Save', command = cmdSave)
# fileMenu.add_command(label='Save As...', command = cmdSaveAs)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command = cmdExit)

#edit menu
editMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Edit', menu = editMenu)

#adding options in edit menu
editMenu.add_command(label='Cut', command = cmdCut)
editMenu.add_command(label='Copy', command = cmdCopy)
editMenu.add_command(label='Paste', command = cmdPaste)
editMenu.add_command(label='Delete', command = cmdClear)
editMenu.add_separator()
editMenu.add_command(label='Find...', command = cmdFind)
editMenu.add_separator()
editMenu.add_command(label='Select All', command = cmdSelectAll)
#tbh i just added this for fun :)


#help menu help help delp
helpMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Help', menu = helpMenu)


helpMenu.add_command(label='About Notepad', command = cmdAbout)
helpMenu.add_command(label='Debug Button', command = cmdAbout)

# root.iconbitmap('icon.ico')
#Key strokes
root.bind_all('<Control-Key-s>', lambda event: cmdSave())
root.bind_all('<Control-Key-c>', lambda event: cmdCopy())
root.bind_all('<Control-Key-v>', lambda event: cmdPaste())
notepad.pack()
root.mainloop()
