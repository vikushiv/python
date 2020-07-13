import sqlite3 as lite

def Youtube_tag_Management(object):
    def __init__(self):
        global brigd
        try:
            brigd=lite.connect("Youtube_tag_Management.db")
            with brigd:
                cur=brigd.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT , description TEXT, tags ")

        except Exception:
            print("Unable to connect DB !")
