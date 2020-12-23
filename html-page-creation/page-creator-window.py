

import webbrowser
from tkinter import *
from pagemaker import makePage

window = Tk()
window.title("Webpage Creator")

# creates a frame to contain lbl, txt, and btn
# this keeps the content centered if the window expands
windowFrame = Frame(window)
windowFrame.pack()

lbl = Label(windowFrame,anchor=CENTER,text="Enter your desired content:")
lbl.configure(font=("Helvetica", 14))
lbl.grid(column=0,row=0,  pady=16)

txt = Text(windowFrame,wrap=WORD,width=36,height=10)
txt.grid(column=0, row=1, padx=25)

def clicked():
    # gets all text in the box
    user_content = txt.get('1.0', END)
    print(user_content)
    # ---from pagemaker.py---
    # we pass the text to a function that
    # creates and opens the page in a new tab
    makePage(user_content)

btn = Button(windowFrame,anchor=CENTER, text="Make my page!", command=clicked)
btn.grid(column=0,row=2, pady=16)


window.mainloop()

