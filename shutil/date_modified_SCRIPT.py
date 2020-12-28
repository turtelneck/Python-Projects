import shutil, time, os

source = './A/'
destination = './B/'
# gets all files in source folder
files_before = os.listdir(source)
count = 0

# iterates through all files in source folder
for i in files_before:
    lastMod = os.path.getmtime(source+i)
    now = time.time()
    day = 60*60*24
    
    # only moves files modified within last 24 hours
    if lastMod > now - (1*day):
        shutil.move(source+i, destination)
        print("--",i)
        count += 1

print("\n{} files have been moved.\n".format(count))

# the following code will allow the user to move the files back
if count > 0:
    
    files_after = os.listdir(destination)

    reset = input("\nReset files? (y/n) \n> ")

    if reset.lower() == "y":
    	# get the files in destination folder
        files_after = os.listdir(destination)
        # iterates through all files in destination folder
        for i in files_after:
            lastMod = os.path.getmtime(destination+i)
            now = time.time()
            day = 60*60*24
            
            # only moves files modified within last 24 hours
            if lastMod > now - (1*day):
                shutil.move(destination+i, source)
                print("--",i)
                
        print("\n{} files have been moved back.\n".format(count))

    else:
        print("\nHave a great day!\n")



