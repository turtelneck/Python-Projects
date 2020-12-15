import os
import time



def run():

    fPath = input("Enter the absolute path of the folder you'd like to check. \nInclude extra backslashes so the file is read properly: \n(example:  C:\\Users\\\YourName\\\Documents\\\ \n> ")
    fType = input("What type of file are you looking for? \n(example: .txt) \n> ")
    folder = os.listdir(fPath)
    modTime = os.path.getmtime(fPath)

    print("\nFOLDER CONTENTS:\n")
    
    for file in folder:
        # if the file is .txt, print the contents
        if fType in file:
            print(file, " || ", time.ctime(modTime))
            with open(os.path.join(fPath,file)) as f:
                print(f.read())
                f.close()
        # for any other file, just print the name and time last modified
        else:
            print(file, " || ", time.ctime(modTime))

    print("")

    

    
        

    
    


if __name__ == "__main__":
    run()
