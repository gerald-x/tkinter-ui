from utils import Scrollable
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

root = Tk()
root.title("Image Stitch")

# Set window to half the size of screen as well as position it
half_screen_width = round(root.winfo_screenwidth()/2) + 10
half_screen_height = round(root.winfo_screenheight()/2) + 50

root.geometry(f"{half_screen_width}x{half_screen_height}+300+150")
root.config(bg="gray", padx=20, pady=20)

# Make frame occupy full screen
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create Frame
frame = Frame(root, bg="gray")
frame.grid(row=0, column=0)


def get_img_num():
    try:
        img_int = int(img_num.get())
    except:
        error_box = messagebox.showerror(parent=root, title="Input Error", message="Invalid input\n\nInput must be an Integer\n\nDont try to play smart")
        root.destroy()

    frame.destroy()
    input_frame = Frame(root, bg="gray")
    input_frame.grid()
    label = Label(input_frame, text="* Enter the name of image files (with extension). E.g: image_2.jpg", bg="gray", font=font.Font(family="Comic Sans MS", size=11)).grid()
    label = Label(input_frame, text="* Ensure files are in current directory or specify full path", bg="gray", font=font.Font(family="Comic Sans MS", size=11)).grid(sticky="NW", pady=4)

    scrollable = Scrollable(root)
    scrollable.populate(img_int)
    scrollable.grid()


label = Label(frame, text="Enter the number of images", bg="gray", font=font.Font(family="Comic Sans MS", size=14)).grid()
img_num = Entry(frame, font=font.Font(size=15))
img_num.grid(pady=35, ipady=8, ipadx=25)
btn = Button(frame, text="Submit", bg="#e30b5d", padx=20, pady=4, fg="white", command=get_img_num, font=font.Font(family="Comic Sans MS", size=12))
btn.grid()



root.mainloop()