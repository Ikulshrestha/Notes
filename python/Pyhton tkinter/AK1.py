import tkinter as tk
n=tk.Tk() # where n is the name of the main window object
w=tk.Button(m, text='Stop', width=25, command=n.destroy)
w.pack()
n.mainloop()
