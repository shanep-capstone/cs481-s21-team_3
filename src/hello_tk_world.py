import tkinter as tk
import tkinter.messagebox
import pytest
#########################################
# Hello Tkinter Framework World.
#
# Quick hello world using the tkinter 
# framework. 
#
# Prereq:
#   python 3.6+
#       $ sudo apt-get install python3
#   
#   tkinter 
#       $ sudo apt-get install python3-tk
#
# Usage:
#   $ python3 hello_tk_world.py
#########################################
WIDTH = 142

# Starts the party by creating a tkinter ojbect,
# and returning it as the variable called "gui"
def init(): 
    gui = tk.Tk() # Comment this line out to make sure test_gui_init and test_tkinter fail when they should.
    gui.title('hello world')
    gui.geometry("240x320")
    return gui

# Creates a tkinter message box 
def hello_world():
    tk.messagebox.showinfo("???", "Hello Tkinter World!")

# Tkinter button handler function
def button_click(gui_frame):
    button = tk.Button(gui_frame, text="Say Hi", width=WIDTH, command=hello_world)
    button.pack()

# Exits and ends the entire program
def die(gui_frame):
    exit_button = tk.Button(gui_frame, text="Exit", width=WIDTH, command=gui_frame.destroy)
    exit_button.pack()

# Main driver function
def main():
    framework = init() # Comment this line out to make sure the main test_tkinter fails when it should.
    button_click(framework)
    die(framework)
    framework.mainloop()
