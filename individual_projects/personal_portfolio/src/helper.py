import tkinter as tk
from tkinter import ttk
import subprocess
import sys
import os

# Project descriptions shown under each button
PROJECTS = [
    {
        "title": "Project 1 — Tic Tac Toe",
        "desc": "Beat the computer by completing a row, column, or diagonal.",
        "file": "tic.py"
    },
    {
        "title": "Project 2 — Personal Library",
        "desc": "Add, search, remove, and view all your books by title or author.",
        "file": "personalLibrary.py"
    },
    {
        "title": "Project 3 — Morse Code Translator",
        "desc": "Translate between English and Morse code, or browse the alphabet.",
        "file": "morse_code.py"
    },
    {
        "title": "Project 4 — Financial Calculator",
        "desc": "Savings goals, compound interest, budgets, sale prices, and tips.",
        "file": "financial_calculator.py"
    },
]

def run_in_terminal(filepath):
    # Get the full path to the project file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, filepath)
    # Open in a new terminal window based on the operating system
    if sys.platform == "win32":
        subprocess.Popen(["start", "cmd", "/k", sys.executable, full_path], shell=True)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", "-a", "Terminal", full_path])
    else:
        subprocess.Popen(["x-terminal-emulator", "-e", sys.executable, full_path])

def create_gui():
    # Create and configure the main window
    root = tk.Tk()
    root.title("Personal Portfolio")
    root.geometry("500x480")
    root.configure(bg="#f5f5f0")
    return root

def create_buttons(root):
    # Title label
    tk.Label(
        root, text="My Projects",
        font=("Helvetica", 18, "bold"),
        bg="#f5f5f0", fg="#1a1a1a"
    ).pack(pady=(24, 2))

    # Subtitle label
    tk.Label(
        root, text="Select a project to launch it in a new terminal window.",
        font=("Helvetica", 10),
        bg="#f5f5f0", fg="#888"
    ).pack(pady=(0, 16))

    # Create a card button for each project
    for project in PROJECTS:
        # Outer card frame
        card = tk.Frame(root, bg="white", bd=0, highlightthickness=1, highlightbackground="#e0e0e0")
        card.pack(fill="x", padx=32, pady=6, ipady=10)

        # Inner frame for padding
        inner = tk.Frame(card, bg="white")
        inner.pack(fill="x", padx=14, pady=4)

        # Project title
        tk.Label(
            inner, text=project["title"],
            font=("Helvetica", 11, "bold"),
            bg="white", fg="#1a1a1a", anchor="w"
        ).pack(fill="x")

        # Project description
        tk.Label(
            inner, text=project["desc"],
            font=("Helvetica", 9),
            bg="white", fg="#888", anchor="w", wraplength=360, justify="left"
        ).pack(fill="x", pady=(2, 6))

        # Launch button
        file = project["file"]
        tk.Button(
            inner, text="Launch  ›",
            font=("Helvetica", 9),
            bg="#f0f0f0", fg="#333",
            relief="flat", cursor="hand2",
            command=lambda f=file: run_in_terminal(f)
        ).pack(anchor="w")

def main_gui():
    # Build and launch the GUI
    root = create_gui()
    create_buttons(root)
    root.mainloop()

#Run
if __name__ == "__main__":
    main_gui()