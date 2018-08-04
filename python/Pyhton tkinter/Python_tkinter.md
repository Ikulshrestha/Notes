# <center>Introduction</center>
 It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with tkinter outputs the fastest and easiest way to create the GUI applications.

 **Steps to create tkinter**:
  1. Importing the module – tkinter
  2. Create the main window (container)
  3. Add any number of widgets to the main window
  4. Apply the event Trigger on the widgets.

         Importing tkinter is same as importing any other module in the python code.
          Note that the name of the module in Python 2.x is ‘Tkinter’ and in Python 3.x
          is ‘tkinter’.  
*There are two main methods used you the user need to remember while creating the Python application with GUI.*

1. **Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1) :**
To create a main window, tkinter offers a method ‘Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)’. To change the name of the window, you can change the className to the desired one.

2. **mainloop() :** There is a method known by the name mainloop() is used when you are ready for the application to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.

*tkinter also offers access to the geometric configuration of the widgets which can organize the widgets in the parent windows. There are mainly three geometry manager classes class.*

  1. **pack() method** : It organizes the widgets in blocks before placing in the parent widget.
  2. **grid() method** : It organizes the widgets in grid (table-like structure) before placing in the parent widget.
  3. **place() method** : It organizes the widgets by placing them on specific positions directed by the programmer.

There are a number of widgets which you can put in your tkinter application. Some of the major widgets are explained below:

   1.  **Button** : To add a button in your application, this widget is used.The general syntax is :
   ```python
   w=Button(master,option=value)
   # EXAMPLE
   w=tk.Button(m, text='Stop', width=25, command=m.destroy)
   ```
master is the parameter used to represent the parent window.
Number of options can be passed as parameters separated by commas. Some of them are listed below.
+ **activebackground** : to set the background color when button is under the cursor.
+ **activeforeground** : to set the foreground color when button is under the cursor.
+ **bg**: to set he normal background color.
+ **command** : to call a function.
+ **font**: to set the font on the button label.
+ **image** : to set the image on the button.
+ **width** : to set the width of the button.
+ **height** : to set the height of the button.

*Simple example of buton* :
```Python
import tkinter as tk
m=tk.Tk() # where m is the name of the main window object
w=tk.Button(m, text='Stop', width=25, command=m.destroy)
w.pack()
m.mainloop()
```
