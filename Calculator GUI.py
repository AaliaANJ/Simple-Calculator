'''
Name: Aalia Anjum
Date: July 29th 2024

Description: The following is code creating a simple TKINTER GUI calculator
#link to video tutorial this is inspred by: https://youtu.be/RF9l5wnFH4M?si=zgDcVvzonsu6bGUb
'''

# importing the relevent libraries
import tkinter as tk
from tkinter import *




# creating a blank feild text space 
f_text = ''

# this is the function that edits the contents of the feild, takes the parameter user_input
def add_to_f (user_input):
    
    # makes the var feild_text editable inside and outside the func
    global f_text 
    # adds any user input to the feild text
    f_text = f_text + str(user_input)
    # deletes any previous text in the feild_text from the first caracter(1.0) to the last caracter (end) of the str
    f.delete('1.0', 'end')
    # inserting the new feild text into the feild at the position (1.0) of the str
    f.insert('1.0', f_text)
    
#the function calculates whatever was typed into the feild text when "=" is pressed
def calculate(): 
    # makes the var feild_text editable inside and outside the func
    global f_text
    # (eval) eveluats the entered feild text str as ints, converts the output back into a str, and stres the output in var results
    results = str(eval(f_text))
    # deletes any previous text in the feild_text from the first caracter(1.0) to the last caracter (end) of the str
    f.delete('1.0', 'end')
    # inserting the results into the feild at the position (1.0) of the str
    f.insert('1.0', results)


# the function clears the feild_text box 
def clear(): 
    # makes the var feild_text editable inside and outside the func
    global f_text
    # makes the feild text balnk again 
    f_text = ''
     # deletes any visible previous text in the feild_text from the first caracter(1.0) to the last caracter (end) of the str
    f.delete('1.0', 'end')


    
#creating a GUI window using Tkinter as tk
window = tk.Tk()
# renaming the window application
window.title('Simple Calculator')
# defining the size of the window
window.geometry('320x270')
#adding the icon
window.iconbitmap('calc.ico')
#displays the feild_text on the window
f = tk.Text(window, height = 2, width = 21, font = ("Arial", 20), bg = 'white')
#the feild box is put on the window by defining its size and place onthe grid
f.grid(row=1, column=1, columnspan=4)



######################################################################################
# creating number buttons on the calc
#######################################################################

# this makes the first btn #1 , it calls the add_ to feild func. the command = lambda: add_to_feild, allows to program to exicute that function
btn_1 = tk.Button(window,text='1', command = lambda: add_to_f(1), width = 5, font = ('Arial', 14), bg = 'light goldenrod')
btn_1.grid(row=4, column = 1)

btn_2 = tk.Button(window,text='2', command = lambda: add_to_f(2), width = 5, font = ('Arial', 14), bg = 'light goldenrod')
btn_2.grid(row=4, column = 2)

btn_3= tk.Button(window,text='3', command = lambda: add_to_f(3), width = 5, font = ('Arial', 14), bg = 'light goldenrod')
btn_3.grid(row=4, column = 3)

btn_4= tk.Button(window,text='4', command = lambda: add_to_f(4), width = 5, font = ('Arial', 14), bg = 'light goldenrod')
btn_4.grid(row=3, column = 1)

btn_5= tk.Button(window,text='5', command = lambda: add_to_f(5), width = 5, font = ('Arial', 14), bg = 'light goldenrod')
btn_5.grid(row=3, column = 2)

btn_6= tk.Button(window,text='6', command = lambda : add_to_f(6), width = 5, font = ('Arial', 14), bg = 'light goldenrod')
btn_6.grid(row=3, column = 3)

btn_7= tk.Button(window,text='7', command = lambda: add_to_f(7), width = 5, font = ('Arial', 14), bg = 'light goldenrod')
btn_7.grid(row=2, column = 1)

btn_8= tk.Button(window,text='8', command = lambda: add_to_f(8), width = 5, font = ('Arial', 14), bg = 'light goldenrod')
btn_8.grid(row=2, column = 2)

btn_9= tk.Button(window,text='9', command = lambda: add_to_f(9), width = 5, font = ('Arial', 14), bg = 'light goldenrod')
btn_9.grid(row=2, column = 3)

btn_0= tk.Button(window,text='0', command = lambda: add_to_f(0), width = 5, font = ('Arial', 14), bg = 'light goldenrod')
btn_0.grid(row=5, column = 1)

######################################################################################
# creating opperations buttons on the calc
#######################################################################

btn_plus=tk.Button(window, text='+', command=lambda: add_to_f('+'), width = 5, font= ('Arial', 14), bg = 'DarkOliveGreen3')
btn_plus.grid(row=4 ,column=4)

btn_minus= tk.Button(window, text='-', command=lambda: add_to_f('-'), width = 5, font= ('Arial', 14) ,bg = 'DarkOliveGreen3')
btn_minus.grid(row=5 ,column=4)

btn_times = tk.Button(window, text='*', command=lambda: add_to_f('*'), width = 5, font= ('Arial', 14) ,bg = 'DarkOliveGreen3')
btn_times.grid(row=3 ,column=4)

btn_division = tk.Button(window, text='/', command=lambda: add_to_f('/'), width = 5, font= ('Arial', 14) ,bg = 'DarkOliveGreen3')
btn_division.grid(row=2 ,column=4)

#clear btn calls the clear func instead of the add to feild func
btn_clear = tk.Button(window, text='clear', command=lambda: clear(), width = 5, font= ('Arial', 14) ,bg = 'gold')
btn_clear.grid(row=5 ,column=3)

btn_decimal = tk.Button(window, text='.', command=lambda: add_to_f('.'), width = 5, font= ('Arial', 14) ,bg = 'light goldenrod')
btn_decimal.grid(row=5 ,column=2)

btn_braket_left= tk.Button(window, text='(', command=lambda: add_to_f('('), width = 5, font= ('Arial', 14) ,bg = 'light goldenrod')
btn_braket_left.grid(row=6 ,column=1)

btn_braket_right= tk.Button(window, text=')', command=lambda: add_to_f(')'), width = 5, font= ('Arial', 14) ,bg = 'light goldenrod')
btn_braket_right.grid(row=6 ,column=2)

#calls the calculate func, this btn spans 2 cells, therefore columnspan = 2 is added and btn width 13 is added instead of 5
btn_equals =  tk.Button(window, text='=', command=lambda: calculate(), width = 12, font= ('Arial', 14) ,bg = 'DarkOliveGreen3')
btn_equals.grid(row=6 ,column=3, columnspan = 2 )


#shows the window all the time untill be press the close btn
window.mainloop()





