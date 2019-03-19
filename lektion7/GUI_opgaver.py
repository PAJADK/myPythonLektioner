import tkinter as tk
from tkinter import messagebox

def change():
    # pass
    if len(entry.get()) == 0:
        #root.withdraw()
        #labelTxt.config(text=" Input felten er tom!!!!")
        tk.messagebox.showwarning("Warning", "Warning message", icon='warning')
    else:
        labelTxt.config(text=entry.get())


def NewFile():
    print("New File!")


def OpenFile():
    print("Open file")


def About():
    print("This is a simple example of a menu")


root = tk.Tk()
root.title("********* TKinter ********")



# message box display
#tk.messagebox.showerror("Error", "Error message")
#tk.messagebox.showwarning("Warning", "Warning message")
#tk.messagebox.showinfo("Information", "Informative message")


menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

#menu.pack()

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
scroll = tk.Scrollbar(frame)
txt = tk.Text(frame, height=4, width=50)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
txt.pack(side=tk.LEFT, fill=tk.Y)
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

txt.insert(tk.END, quote)

""" Opgave 4 - Entry widget """
frame2 = tk.Frame(root)
frame2.pack()

labelTxt2 = tk.Label(frame2, text="Indtast navn:")
labelTxt2.pack(side=tk.LEFT, padx=10, pady=10)

entry = tk.Entry(frame2)
entry.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
