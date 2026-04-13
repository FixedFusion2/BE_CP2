#TE 2nd Personal Portfolio Helper Functions
#Import libraries
import tkinter as tk
from tkinter import ttk

#Create GUI with title and size
def create_gui():
    root = tk.Tk()
    root.title("Personal Portfolio")
    root.geometry("800x600")
    return root
#Create buttons to click and display project information and when project button is clicked run the project
def create_buttons(root):
    button1 = ttk.Button(root, text="Project 1", command=project1)
    button1.pack(pady=10)
    button2 = ttk.Button(root, text="Project 2", command=project2)
    button2.pack(pady=10)
    button3 = ttk.Button(root, text="Project 3", command=project3)
    button3.pack(pady=10)
#Functions to run when project buttons are clicked
def project1():
    print("Project 1: Personal Portfolio Website")
def project2():
    print("Project 2: Data Analysis with Python")
def project3():
    print("Project 3: Machine Learning Model")
def project4():
    print("Project 4: Mobile App Development")

def main():
    root = create_gui()
    create_buttons(root)
    root.mainloop()

if __name__ == "__main__":
    main()