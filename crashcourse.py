import sqlite3 as lite

#Functionality goes hear

class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con=lite.connect('courses.db')
            with con:
                cur=con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT , description TEXT, price TEXT,isPrivate BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to connect to a DB !")

    #inserting data to database        
    def insert_data(self,data):
        try:
            with con:
                cur=con.cursor()
                cur.execute("INSERT INTO course(name,description,price,isPrivate) VALUES (?,?,?,?)",data)
            return True
        except Exception:
            return "something wrong in insert data"

    # fetching data from database
    def fetch_data(self):
        try:
            with con:
                cur=con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return True

    #deleting data on database
    def delete_data(self,id):
        try:
            with con:
                cur=con.cursor()
                sql="DELETE FROM course WHERE id=?"
                cur.execute(sql,[id])
                return True 
        except Exception:
            return True


#interface to user

def main():
    print("*"*40)
    print("\n  ::  Course Management  ::\n")
    print("*"*40)
    print("\n")

    db=DatabaseManage()

    print("#"*40)
    print("\n  :: User Manual ::\n")
    print("#"*40)
    print('\n Press 1. Insert a new Course\n')
    print('Press 2. show all Course\n')
    print('Press 3. Delete a course (NEED ID OF COURSE)\n')
    print("#"*40)
    print("\n")


    while True:
        choice=input("\n Enter a CHoice: ")

        #TODO: MAKE IT WITH LOOP
            

        if choice=="1":
            name=input("\n Enter Course name: ")
            description=input("\n Enter Course description: ")
            price=input("\n Enter Course Price: ")
            private=input("\n Is this course private (0 or 1): ")

            if db.insert_data([name,description,price,private]):
                print("\nCourse was inserted successfully ")
            else:
                print("\nSomething went Wrong")
            cont=input("\nDo yo want to do more operation (0 or 1): ")
        elif choice=="2":
            print("\n:: Course list ::")

            for index,item in enumerate(db.fetch_data()):
                print("\n Sl no : "+str(index+1))
                print("course ID : "+str(item[0]))
                print("course name : "+str(item[1]))
                print("course description : "+str(item[2]))
                print("course price : "+str(item[3]))

                private ="Yes" if item[4] else 'NO'
                print("course is private or not : "+private)
                print("\n")
            cont=input("\nDo yo want to do more operation (0 or 1): ")

        elif choice=="3":
            record_id=input("Enter the course id: ")

            if db.delete_data(record_id):
                print("course id deleted")
            else:
                print("Something went wrong")
            cont=input("\nDo yo want to do more operation (0 or 1): ")
        
        else:
            print("\n BAD CHOICE")
            cont=input("\nDo yo want to do more operation (0 or 1): ")
        if(cont=="0"):
            break


if __name__ == "__main__":
    main()


#todo:i want to create a exact same application which we have crreated just now name description 