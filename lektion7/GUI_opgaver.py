import tkinter as tk
from tkinter import *


def change():
   # pass
   labelTxt.config(text=entry.get())


root = tk.Tk()
root.title("********* TKinter ********")
"""Her laver vi en frame og packer den ned i root vinduet."""
frame = tk.Frame(root)
frame.pack()

""" Opgave 1 - Labels """
labelTxt = tk.Label(frame, text="Hej, velkommen til mit program\n\n\n")
labelTxt.pack()

""" Opgave 2 - Buttons """
button1 = tk.Button(frame, text="Quit", fg="red", command=quit)
button1.pack()

button2 = tk.Button(frame, text="Change text", command=change)
button2.pack()

""" Opgave 3 - Text widget """
scroll = Scrollbar(frame)
txt = tk.Text(frame, height=4, width=50)
scroll.pack(side=RIGHT, fill=Y)
txt.pack(side=LEFT, fill=Y)
scroll.config(command=txt.yview)
txt.config(yscrollcommand=scroll.set)

quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""

txt.insert(END, quote)

""" Opgave 4 - Entry widget """
frame2 = tk.Frame(root)
frame2.pack()

labelTxt2 = tk.Label(frame2, text="Indtast navn:")
labelTxt2.pack(side=tk.LEFT, padx= 10, pady=10)

entry = tk.Entry(frame2)
entry.pack(side=tk.LEFT, padx= 10, pady=10)


root.mainloop()
