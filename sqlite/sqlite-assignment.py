
import sqlite3


conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    # db created
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        string TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('assignment.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    for x in fileList:
        if '.txt' in x:
            # adds anything with '.txt' into the db
            cur.execute("REPLACE INTO tbl_files(string) VALUES (?)", \
                        (('{}').format(x),)) # .format adds the file name to the sql command
            # if a file gets added, print it to the console
            print(x)
    conn.commit()
conn.close()
