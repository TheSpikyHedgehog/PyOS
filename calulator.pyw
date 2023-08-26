from tkinter import *
import tkinter.messagebox

import sys, math, random
def cal():
    root = Tk()
    root.title("PyCal")
    root.iconbitmap("PyOS/start.ico")
    root.geometry("320x380")
    root.resizable(False, False)
    root.deiconify()
    root.record('blorg')
    root.configure(bg='LightBlue')
    def exit():
        root.destroy
        sys.exit("User quit")
    def button_click(item):
        global expression
        expression = expression + str(item)
        input_text.set(expression)

    def btn_clear():
        global expression
        expression = ""
        input_text.set("")
    def equal_btn():
        try:
            global expression
            result = str(eval(expression))
            input_text.set(result)
            expression = ""
        except SyntaxError:
            tkinter.messagebox.showerror(title="Error: Invalid Input.", message="Complete your expression or check if you have used words in your prompt.")
    expression = ""
    input_text = StringVar()

    input_frame = Frame(root, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
    input_frame.pack(side = TOP)
    input_field = Entry(input_frame, font = ("Tahoma", 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
    input_field.grid(row = 0, column = 0)
    input_field.pack(ipady = 10)
    btn_frame = Frame(root, width = 312, height = 272.5, bg = "grey")
    btn_frame.pack()
    #BUTTIONS! yay!
    clear = Button(btn_frame, text = "Clear", fg = "yellow", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
    divide = Button(btn_frame, text = "/", fg = "blue", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: button_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
    seven = Button(btn_frame, text = "7", fg = "brown", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
    eight = Button(btn_frame, text = "8", fg = "red", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
    nine = Button(btn_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
    multiply = Button(btn_frame, text = "x", fg = "orange", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: button_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
    four = Button(btn_frame, text = "4", fg = "orange", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
    five = Button(btn_frame, text = "5", fg = "purple", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
    six = Button(btn_frame, text = "6", fg = "green", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
    minus = Button(btn_frame, text = "-", fg = "indigo", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: button_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
    one = Button(btn_frame, text = "1", fg = "orange", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
    two = Button(btn_frame, text = "2", fg = "blue", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
    three = Button(btn_frame, text = "3", fg = "red", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
    plus = Button(btn_frame, text = "+", fg = "orange", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: button_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
    zero = Button(btn_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
    point = Button(btn_frame, text = ".", fg = "purple", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: button_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
    equals = Button(btn_frame, text = "=", fg = "brown", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: equal_btn()).grid(row = 4, column = 3, padx = 1, pady = 1)



    # Keyboard inputs
    root.bind('0', lambda event: button_click(0))
    root.bind('1', lambda event: button_click(1))
    root.bind('2', lambda event: button_click(2))
    root.bind('3', lambda event: button_click(3))
    root.bind('4', lambda event: button_click(4))
    root.bind('5', lambda event: button_click(5))
    root.bind('6', lambda event: button_click(6))
    root.bind('7', lambda event: button_click(7))
    root.bind('8', lambda event: button_click(8))
    root.bind('9', lambda event: button_click(9))
    root.bind('<Return>', lambda event: equal_btn())
    root.bind('<Escape>', lambda event: exit())
    root.bind('<+>', lambda event: button_click("+"))
    root.bind('</>', lambda event: button_click("/"))
    root.bind('<.>', lambda event: button_click("."))
    root.bind('<KP_Subtract>', lambda event: button_click("-"))
    root.bind('-', lambda event: button_click("-"))
    root.bind('Backspace', lambda event: btn_clear())
    root.mainloop() 
cal()