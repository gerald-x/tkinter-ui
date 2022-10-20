import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
from stitch import stitch_img


class Scrollable(tk.Frame):
    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.status_done = False
        self.canvas = tk.Canvas(self, borderwidth=0, background="gray")
        self.frame = tk.Frame(self.canvas, background="gray")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)


    def populate(self, number):
        '''Put in some data'''
        self.img_input = [
            Entry(self.frame, font=font.Font(size=12)) for _ in range(number)
        ]

        display = [name.grid(pady=12, ipady=8, ipadx=35, sticky="NW") for name in self.img_input]

        Button(self.frame, text="Submit", bg="#e30b5d", padx=20, pady=4, fg="white", command=self.submit_img, font=font.Font(family="Comic Sans MS", size=12)).grid(pady=10)


    def submit_img(self):
        self.blank_inputs = list(filter(lambda x: not x.get().strip(), self.img_input))
        self.inputs = list(filter(lambda x: (not x.get().strip()) == False, self.img_input)) 

        if self.blank_inputs:
            messagebox.showerror(parent=self.frame, title="Input Error", message="Make sure all input fields are filled\n\nDont try to play smart")
        else:
            img_fnames = [x.get() for x in self.inputs]
            
            stitched_image = stitch_img(img_fnames)
            success_message = Toplevel(self.canvas)
            success_message.mainloop()

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))



if __name__ == "__main__":
    root=tk.Tk()
    example = Scrollable(root)
    example.populate(50)
    print(example.img_input)
    example.pack(side="top", fill="both", expand=True)
    root.mainloop()