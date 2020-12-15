
import sqlite3


conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        string TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("REPLACE INTO tbl_files(string) VALUES (?)", \
                ('information.docx',))
    cur.execute("REPLACE INTO tbl_files(string) VALUES (?)", \
                ('Hello.txt',))
    cur.execute("REPLACE INTO tbl_files(string) VALUES (?)", \
                ('myImage.png',))
    cur.execute("REPLACE INTO tbl_files(string) VALUES (?)", \
                ('myMovie.mpg',))
    cur.execute("REPLACE INTO tbl_files(string) VALUES (?)", \
                ('World.txt',))
    cur.execute("REPLACE INTO tbl_files(string) VALUES (?)", \
                ('data.pdf',))
    cur.execute("REPLACE INTO tbl_files(string) VALUES (?)", \
                ('myPhoto.jpg',))
    conn.commit()
conn.close()


conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_files WHERE string LIKE '%.txt'")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "File:  {}".format(item[1])
        print(msg)
