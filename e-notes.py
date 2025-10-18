#notes that you can write down


from time import sleep
import sqlite3
print("Welcome to E-JOURNAL")
print("You need to sign up before you begin")




# Making accounts
def createTable():
    with sqlite3.connect("account.db")as db:
        cursor = db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS accountInfo
            (account_id integer Primary Key,
            account_username text,
            account_password text);
            """
        cursor.execute(sql)
def createAccount():
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    values = (username, password)
    with sqlite3.connect("account.db")as db:
        cursor = db.cursor()
        sql = """INSERT INTO accountInfo (account_username, account_password)
            values(?, ?)
            """

    cursor.execute(sql, values)
    db.commit()

#LOGGING IN VERIFYING CREDENTIALS

def login(username, password):
    with sqlite3.connect("account.db") as db:
        cursor = db.cursor()
        sql = """SELECT COUNT(*) FROM accountInfo
        WHERE account_username = ? AND account_password = ?
        """
        
    cursor.execute(sql, (username, password))
    result = cursor.fetchone()
    return result[0] > 0

    
    
#THIS IS WHERE YOU'D PUT THE INTRO TO YOUR OS    
    
def start():
    createTable()
    print("Welcome to whatever this is (THIS IS WHERE U PUT UR STARTING OS SYSTEM")
    option = int(input("1. Sign Up, 2. Login: "))
    if option == 1:
        createAccount()

    if option == 2:
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        if login(username,password):
            print("Login Successful")

        else:
            print("Account not found")


start()
begin_notes = (input("Do you want to start writing notes "))
if begin_notes == "Yes" or begin_notes == "yes":
   title_notes = (input("What do you want to call your notes "))
   centered_text = title_notes.center(20)
   print("")
   print("")
   print(centered_text,":")
   print("___________________")
   
    
   while begin_notes == "Yes" or begin_notes == "yes":
       notes = (input(""))
       sleep(20)
       print("[1] Continue writing notes")
       print("[2] Exit Notes")
       contd_notes = int(input("Choose one of the above(AS A NUMBER PLEASE!)"))
       if contd_notes == "1":
        print(notes)
        notes = (input(""))
        sleep(20)
        print("[1] Continue writing notes")
        print("[2] Exit Notes")
       elif contd_notes == "2":
          print("Thank you for your patience")
       
       else:
          print("Invalid choice")

           
       


elif begin_notes == "No" or begin_notes == "no":
    print("Thank you for your patience")