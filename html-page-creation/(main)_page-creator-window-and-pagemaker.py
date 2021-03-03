

import webbrowser
from tkinter import *

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
    
    # creates and opens a page in a new tab
    def makePage(content):
        # creates/overwrites any pages previously created
        f = open("new-page.html", "w")
        # adds any text passed to it as an <h1> element
        f.write("<html><body><h1>{}</h1></body></html>".format(content))
        f.close()
	
        # opens created page in new tab
        webbrowser.open_new_tab("new-page.html")
    
    # we pass the text to our function
    makePage(user_content)


btn = Button(windowFrame,anchor=CENTER, text="Make my page!", command=clicked)
btn.grid(column=0,row=2, pady=16)


window.mainloop()

