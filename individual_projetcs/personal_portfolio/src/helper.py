import tkinter as tk
from tkinter import ttk

from financial_calculator import *
from morse_code import *
from personalLibrary import *
from tic import *

def create_gui():
    root = tk.Tk()
    root.title("Personal Portfolio")
    root.geometry("800x600")
    return root

def create_buttons(root):
    ttk.Button(root, text="Project 1", command=project1).pack(pady=10)
    ttk.Button(root, text="Project 2", command=project2).pack(pady=10)
    ttk.Button(root, text="Project 3", command=project3).pack(pady=10)
    ttk.Button(root, text="Project 4", command=project4).pack(pady=10)

def project1():
    tic_tac_toe()

def project2():
    menu()

def project3():
    main_menu()

def project4():
    main_run()

def main_gui():
    root = create_gui()
    create_buttons(root)
    root.mainloop()

if __name__ == "__main__":
    main_gui()
