import tkinter as tk
m=tk.Tk() # where m is the name of the main window object
w=tk.Button(m, text='Stop', width=25, command=m.destroy)
w.pack()
m.mainloop()