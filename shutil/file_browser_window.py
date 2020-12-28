

from tkinter import *
from tkinter import filedialog
import shutil, time, os


window = Tk()
window.title("Webpage Creator")

# frames are used to keep all content arranged
# at the center if the window expands
introContainer = Frame(window)
introContainer.pack()

browsingContainer = Frame(window)
browsingContainer.pack()

executionContainer = Frame(window)
executionContainer.pack()


# opens the file explorer window
def browseFiles():
    filename = filedialog.askdirectory()
    # change label contents
    firstLoc.configure(text=filename)

# identical function for the second button,
# since using the same one for both while passing
# in the label as a param had strange consequences
def browseFiles2():
    filename = filedialog.askdirectory()
    secondLoc.configure(text=filename)


# moves files between the two folders
def fileMover():
    # gets the content of the labels
    source = firstLoc.cget("text")+"/"
    destination = secondLoc.cget("text")+"/"
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

    info.configure(text="{} files have been moved.\n".format(count))

# header/body above file search area
introHeader = Label(introContainer,anchor=CENTER,text="FileMover 1.0")
introHeader.configure(font=("Helvetica", 14))
introHeader.grid(column=0,row=0, padx=16,pady=12)

introBody = Label(introContainer,justify=CENTER,wraplength=240,text="All files modified within the last 24 hours will be moved from folder 1 to folder 2")
introBody.configure(font=("Helvetica", 9))
introBody.grid(column=0,row=1, padx=16,pady=4)
# file search area
browse1 = Button(browsingContainer,anchor=CENTER,text="Browse...", command=browseFiles)
browse1.grid(column=0,row=0, padx=16,pady=16)

firstLoc = Label(browsingContainer,anchor=CENTER,text="please select the location of folder 1")
firstLoc.configure(font=("Helvetica", 9))
firstLoc.grid(column=1,row=0, padx=16,pady=16)

browse2 = Button(browsingContainer,anchor=CENTER,text="Browse...", command=browseFiles2)
browse2.grid(column=0,row=1, padx=16,pady=16)

secondLoc = Label(browsingContainer,anchor=CENTER,text="please select the location of folder 2")
secondLoc.configure(font=("Helvetica", 9))
secondLoc.grid(column=1,row=1, padx=16,pady=16)
# executor button and all else below that
exec = Button(executionContainer,anchor=CENTER, text="Move My Files!", command=fileMover)
exec.grid(column=0,row=0, padx=16,pady=16)

info = Label(executionContainer,anchor=CENTER, text="")
info.configure(font=("Helvetica", 9))
info.grid(column=0,row=1, padx=16,pady=16)




window.mainloop()
