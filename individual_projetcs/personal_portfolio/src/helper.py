import tkinter as tk
from tkinter import ttk
import subprocess
import sys
import os

def create_gui():
    root = tk.Tk()
    root.title("Personal Portfolio")
    root.geometry("800x600")
    return root

def create_buttons(root):
    ttk.Button(root, text="Project 1 - Tic Tac Toe",       command=project1).pack(pady=10)
    ttk.Button(root, text="Project 2 - Personal Library",   command=project2).pack(pady=10)
    ttk.Button(root, text="Project 3 - Morse Code",         command=project3).pack(pady=10)
    ttk.Button(root, text="Project 4 - Financial Calc",     command=project4).pack(pady=10)

def run_in_terminal(filepath):
    # Gets the folder this file is in
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, filepath)

    if sys.platform == "win32":
        # Windows: opens a new Command Prompt window
        subprocess.Popen(["start", "cmd", "/k", sys.executable, full_path], shell=True)
    elif sys.platform == "darwin":
        # Mac: opens a new Terminal window
        subprocess.Popen(["open", "-a", "Terminal", full_path])
    else:
        # Linux
        subprocess.Popen(["x-terminal-emulator", "-e", sys.executable, full_path])

def project1():
    run_in_terminal("tic.py")

def project2():
    run_in_terminal("personalLibrary.py")

def project3():
    run_in_terminal("morse_code.py")

def project4():
    run_in_terminal("financial_calculator.py")

def main_gui():
    root = create_gui()
    create_buttons(root)
    root.mainloop()

if __name__ == "__main__":
    main_gui()