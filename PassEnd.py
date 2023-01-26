import sqlite3
import sys
import subprocess
import argon2

# Create new table if needed!
def create():
    connect = sqlite3.connect('passwords.db')
    cur = connect.cursor()
    cur.execute("""CREATE TABLE passwords (
                website text,
                email text,
                user text,
                password text
    )""")
    connect.commit()
    connect.close()


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def create_new_login():
    connect = sqlite3.connect('login_password.db')
    cur = connect.cursor()
    cur.execute("""CREATE TABLE login (
                login_password text,

    )""")
    connect.commit()
    connect.close()

def add_login(password):
    connect = sqlite3.connect('login_password.db')
    cur = connect.cursor()
    cur.execute("INSERT INTO passwords VALUES (?,?,?,?)", (password))
    connect.commit()
    connect.close()

def login():
    dec = input("Do you have a login password? (Y/N)")
    if dec == 'N':
        login_pass = input("Make a password for enter!")
        create_new_login()
        add_login(login_pass)
        print("You made a new password!")

    elif dec == 'Y':
        pass  # type in password
    else:
        print("Please put a 'Y' or 'N' please!")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def clear_screen(): #need to get this working, to make the display look nicer
    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls',shell=True)
    else:
        subprocess.run('cls', shell=True)

def add(website,email,user,password):
    connect = sqlite3.connect('passwords.db')
    cur = connect.cursor()
    cur.execute("INSERT INTO passwords VALUES (?,?,?,?)", (website, email, user, password))

    connect.commit()
    connect.close()

def check_dup():
    connect = sqlite3.connect('passwords.db')
    cur = connect.cursor()
    cur.execute("""DELETE from passwords WHERE EXISTS (
    SELECT 1 FROM passwords p2
    WHERE passwords.website = p2.website
    AND passwords.rowid > p2.rowid
    )""")

    connect.commit()
    connect.close()
def delete(id):
    connect = sqlite3.connect('passwords.db')
    cur = connect.cursor()
    cur.execute("DELETE from passwords WHERE rowid = (?)",id)
    connect.commit()
    connect.close()

def update(email, user, password, id): #need to fix, if not then having 3 def for each value is fine
    connect = sqlite3.connect('passwords.db')
    cur = connect.cursor()
    cur.execute("""UPDATE passwords SET email = (?) AND user = (?) AND password = (?)
                WHERE rowid = (?)
    """, (email, user, password, id,))
    connect.commit()
    connect.close()

def email_update(email, id):
    connect = sqlite3.connect('passwords.db')
    cur = connect.cursor()
    cur.execute("""UPDATE passwords SET email = (?)
                WHERE rowid = (?)
    """, (email, id))
    connect.commit()
    connect.close()

def user_update(user, id):
    connect = sqlite3.connect('passwords.db')
    cur = connect.cursor()
    cur.execute("""UPDATE passwords SET user = (?)
                WHERE rowid = (?)
    """, (user, id))
    connect.commit()
    connect.close()

def password_update(password, id):
    connect = sqlite3.connect('passwords.db')
    cur = connect.cursor()
    cur.execute("""UPDATE passwords SET password = (?)
                WHERE rowid = (?)
    """, (password, id))
    connect.commit()
    connect.close()

def display():
    global value
    value = ()
    connect = sqlite3.connect('passwords.db')
    cur = connect.cursor()
    list = cur.execute("SELECT rowid, * FROM passwords")
    for l in list:
        if len(l) == 0:
            print("You have no passwords added")
        else:
            print(f'\nID: {l[0]}\n'
                f'Website: {l[1]}\n'
                f'Email: {l[2]}\n'
                f'Username: {l[3]}\n'
                f'Password: {l[4]}\n'
                f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
        if list == None: #try to get this working
            print("There is no information in the data base yet!")
    connect.commit()
    connect.close()

def one_look(website):
    connect = sqlite3.connect('passwords.db')
    cur = connect.cursor()
    cur.execute("SELECT rowid,* from passwords WHERE website = (?)",(website,))
    websites = cur.fetchall()
    for l in websites:
        print(f'ID: {l[0]}\n'
              f'Website: {l[1]}\n'
              f'Email: {l[2]}\n'
              f'Username: {l[3]}\n'
              f'Password: {l[4]}\n'
              f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    connect.commit()
    connect.close()


def drop():
    connect = sqlite3.connect('passwords.db')
    cur = connect.cursor()
    cur.execute("DROP TABLE passwords")

def order():
    connect = sqlite3.connect('passwords.db')
    cur = connect.cursor()
    cur.execute("SELECT rowid, * FROM passwords ORDER BY rowid")

def encryption(input): # returns the hash version of the password inputted
    argon2Hasher = argon2.PasswordHasher(
        time_cost = 3,
        memory_cost = 64,
        parallelism = 1,
        hash_len = 32,
        salt_len = 16
    )
    password = input
    hash = argon2Hasher.hash(password) # hash + salt of password 
    
def verification(input): # returns true if the password is true to the hash and salt 
    argon2Hasher = argon2.PasswordHasher(
        time_cost = 3,
        memory_cost = 64,
        parallelism = 1,
        hash_len = 32,
        salt_len = 16
    )
    password = input

    verifyValid = argon2Hasher.verify(hash, password) # verification: true if the same, false if not the same