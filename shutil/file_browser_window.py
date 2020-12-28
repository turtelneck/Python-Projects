

from tkinter import *
from tkinter import filedialog
import shutil, time, os


window = Tk()
window.title("Webpage Creator")

# creates a frame to contain lbl, txt, and btn
# this keeps the content centered if the window expands
browsingContainer = Frame(window)
browsingContainer.pack()

executionContainer = Frame(window)
executionContainer.pack()


# opens the file explorer window
def browseFiles():
    filename = filedialog.askdirectory()
    # change label contents
    lbl.configure(text=filename)

# identical function for the second button,
# since using the same one for both while passing
# in the label as a param had strange consequences
def browseFiles2():
    filename = filedialog.askdirectory()
    lbl2.configure(text=filename)


# moves files between the two folders
def fileMover():
    # gets the content of the labels
    source = lbl.cget("text")+"/"
    destination = lbl2.cget("text")+"/"
    # creates a list of the files in `source`
    files = os.listdir(source)
    count = 0
    
    for i in files:
        lastMod = os.path.getmtime(source+i)
        now = time.time()
        day = 60*60*24

        # only moves files modified within last 24 hours
        if lastMod > now - (1*day):
            shutil.move(source+i, destination)
            print("--",i)
            count += 1


btn = Button(browsingContainer,anchor=CENTER, text="Browse...", command=browseFiles)
btn.grid(column=0,row=0, padx=16,pady=16)

lbl = Label(browsingContainer,anchor=CENTER,text="this contains your folder address")
lbl.configure(font=("Helvetica", 9))
lbl.grid(column=1,row=0, padx=16,pady=16)

btn = Button(browsingContainer,anchor=CENTER, text="Browse...", command=browseFiles2)
btn.grid(column=0,row=1, padx=16,pady=16)

lbl2 = Label(browsingContainer,anchor=CENTER,text="this contains your folder address")
lbl2.configure(font=("Helvetica", 9))
lbl2.grid(column=1,row=1, padx=16,pady=16)

btn = Button(executionContainer,anchor=CENTER, text="Move My Files!", command=fileMover)
btn.grid(column=0,row=0, padx=16,pady=16)




window.mainloop()
