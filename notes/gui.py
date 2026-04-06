import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.title("Testing")
root.configure(background = "#D5FFFF")
root.minsize(250,250)
root.maxsize(1000,1000)
root.geometry("300x300+100+100")
tk.Label(root, text="MEME CLICKER", font= ("Times New Roman", 30)).pack()
def handle_click():
    print("Button was clicked!")
button = tk.Button(root, text="Click Me", command=handle_click)
button.pack(pady=20)

image_path = "4t2orp.jpg"
img_open = Image.open(image_path)
img_tk = ImageTk.PhotoImage(img_open)

"""button.pack_forget()  # Hides the button
button.pack()         # Shows the button again"""

# Display the image in a Label widget
label = tk.Label(root, image=img_tk)
label.pack()

root.mainloop()