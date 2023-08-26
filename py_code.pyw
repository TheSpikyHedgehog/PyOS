from tkinter import *
import ctypes
import re
import os
from tkinter import simpledialog, messagebox
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText



ctypes.windll.shcore.SetProcessDpiAwareness(True)
try:
    os.mkdir("C:/PyCode")
except FileExistsError:
    print("User already has required directory")
# Setup Tkinter
root = Tk()
root.geometry('1500x1000')
current_file = 'default.py'
root.title(f"{current_file} - PyCode | Python editor")


root.rowconfigure(0, minsize=900, weight=1)
root.columnconfigure(1, minsize=900, weight=1)


#
#-----------------------BUTTON FUNC--------------------------
#
def about():
    messagebox.showinfo(title="About", message=f"PyCode is a python code editor for windows.  It is written in 100% python.")
def clear():
    editArea.delete('1.0', END)
def cut():
    editArea.event_generate("<<Cut>>")
def paste():
    editArea.event_generate("<<Paste>>")
def copy():
    editArea.event_generate("<<Copy>>")
def selectall():
    editArea.event_generate("<<SelectAll>>")
def new_file():
    global current_file
    responce = messagebox.askyesnocancel(title="Save?", message="Do you want to save your file?")
    if responce == True:
        with open(f'C:/PyCode/{current_file}', 'w', encoding='utf-8') as f:
            f.write(editArea.get('1.0', END))
            try:
                f.write(editArea.delete('1.0', END))
            except TypeError:
                print("Perpose error")
    elif False:
        with open(f'C:/PyCode/{current_file}', 'w', encoding='utf-8') as f:
            try:
                f.write(editArea.delete('1.0', END))
            except TypeError:
                print("Perpose error")
    else:
        pass
    
    current_file = simpledialog.askstring("Input", "Name your new file (don't forget to include file format like .py)")
    
    with open(f'C:/PyCode/{current_file}', 'w', encoding='utf-8') as f:
        f.write('')
    root.title(f"{current_file} - PyCode | Python editor")


def placeholder():
    pass

#
#------------------------------------------------------------
#
def open_file(event=None):
    
    filepath = askopenfilename(
        filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    
    clear()
    with open(filepath, "r", encoding="utf-8") as input_file:
        try:
            text = input_file.read()
            editArea.insert(END, text)
        except UnicodeDecodeError:
            messagebox.showerror(title="UnicodeDecodeError", message="The file you are trying to open has illegal multibyte sequences inside it which evoked this error. Go to help for more. ")
            
    blorg = filepath.split("/")
    current_file = blorg[(len(blorg)-1)]

    root.title(f"{current_file} - PyCode | Python editor")

def save_file(event=None):
    
    filepath = askopenfilename(
        defaultextension="py",
        filetypes=[("Python Files", "*.py"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w", encoding="utf-8") as output_file:
        text = editArea.get(1.0, END)
        output_file.write(text)
    blorg = filepath.split("/")
    current_file = blorg[(len(blorg)-1)]
    root.title(f"{current_file} - PyCode | Python editor")
    messagebox.showinfo(title="Success", message="Sucessfully saved file")

def execute(event=None):

    
    with open(f'C:/PyCode/{current_file}', 'w', encoding='utf-8') as f:
        f.write(editArea.get('1.0', END))

   
    os.system(f'start cmd /K "python C:/PyCode/{current_file}"')

# people make changes; add things
def changes(event=None):
    global previousText

    if editArea.get('1.0', END) == previousText:
        return


    for tag in editArea.tag_names():
        editArea.tag_remove(tag, "1.0", "end")

        
    
    i = 0
    for pattern, color in repl:
        for start, end in search_re(pattern, editArea.get('1.0', END)):
            editArea.tag_add(f'{i}', start, end)
            editArea.tag_config(f'{i}', foreground=color)
            # if str(previousText) == 'e':
            #     print("detect")
            # else:
            #     print("NO")
            i+=1
            # print(i)
    previousText = editArea.get('1.0', END) 
    # hold = (len(editArea.get('1.0', END)))
    # print(hold)
    # print(editArea.get(float(hold - 1)))

def search_re(pattern, text, groupid=0):
    matches = []

    text = text.splitlines()
    for i, line in enumerate(text):
        for match in re.finditer(pattern, line):

            matches.append(
                (f"{i + 1}.{match.start()}", f"{i + 1}.{match.end()}")
            )

    return matches


def rgb(rgb):
    return "#%02x%02x%02x" % rgb


previousText = ''


normal = rgb((234, 234, 234))
keywords = rgb((234, 95, 95))
comments = rgb((192,192,192))
string = rgb((152,251,152))
function = rgb((95, 211, 234))
background = rgb((42, 42, 42))
par = rgb((65,105,225))
num = rgb((255,140,0))
font = 'Consolas 15'


main_menu = Menu(root)
root.configure(menu=main_menu)

repl = [
    ['(^| )(False|\\|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)($| )', keywords],
    ['".*?"', string],
    ['\'.*?\'', string], 
    ['#.*?$', comments],
    ['print|=|for|range', par],
    ['0|1|2|3|4|5|6|7|8|9|', num],

]
editArea = ScrolledText(

    root,
    background=background,
    foreground=normal,
    insertbackground=normal,
    relief=FLAT,
    borderwidth=30,
    font=font,
)

editArea.grid(row=0, column=1, sticky="nsew")
fileMenu = Menu(main_menu, tearoff = False)
editMenu = Menu(main_menu, tearoff= False)
helpMenu = Menu(main_menu, tearoff=False)

main_menu.add_cascade(label='File', menu = fileMenu)
fileMenu.add_command(label='New', command = new_file)
fileMenu.add_command(label='Save', command = save_file)
fileMenu.add_command(label='Open', command = open_file)
# fileMenu.add_command(label='Current File', command = show_current_f)
fileMenu.add_command(label='Run', command = execute)

main_menu.add_cascade(label='Edit', menu = editMenu)
editMenu.add_command(label='Select All', command = selectall)
editMenu.add_command(label='Copy', command = copy)
editMenu.add_command(label='Paste', command = paste)
editMenu.add_command(label='Cut', command = cut)
editMenu.add_command(label='Clear', command = clear)

main_menu.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label="About PyCode", command = about)


editArea.insert('1.0', """print("WELCOME TO PyCode!")
#delete this text
print("All files (including this default file) will be located at C:/PyCode/ !")
#You may delete this file as you wish. Note that this file will be recreated everytime you run this.
#Another note: Somefiles may not be readable. This is currently unfixable.
                """)


editArea.bind('<KeyRelease>', changes)
root.bind('<Control-s>', save_file)
# ctrl-r to execute i guess.
root.bind('<Control-r>', execute)

root.bind('<Control-o>', open_file)



changes()
root.mainloop()