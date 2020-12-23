from tkinter import *

root = Tk()
root.title("Fee Fie Foe Fum")

rootFrame=Frame(root, width=300, height=160)
rootFrame.pack()

button1 = Button(rootFrame, text="Mercy!")
button1.place(x=10, y=10, height=30, width=100)

button2 = Button(rootFrame, text="Justice!")
button2.place(x=10, y=50, height=30, width=100)

text1 = Label(rootFrame, text="Verdict:")
text1.place(x=10, y=90)
tbox1 = Text(rootFrame)
tbox1.place(x=10, y=115, height=30, width=200)


root.mainloop()

