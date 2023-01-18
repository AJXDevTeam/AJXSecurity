import PassEnd
import sqlite3
import sys
import subprocess
from SendEmail import Sender
import PassEnd

def deleteTable():
    connect = sqlite3.connect('login.db')
    cur = connect.cursor()
    cur.execute("DROP TABLE login")

def delete_Table():
    connect = sqlite3.connect('email.db')
    cur = connect.cursor()
    cur.execute("DROP TABLE email")

def create_new_login():
    connect = sqlite3.connect('login.db')
    cur = connect.cursor()
    cur.execute("""CREATE TABLE login (
                loginpassword text

    )""")
    connect.commit()
    connect.close()

def create_new_email():
    connect = sqlite3.connect('email.db')
    cur = connect.cursor()
    cur.execute("""CREATE TABLE email (
                email text

    )""")
    connect.commit()
    connect.close()

def add_email(email):
    connect = sqlite3.connect('email.db')
    cur = connect.cursor()
    cur.execute("INSERT INTO email VALUES (?)", (email,))
    connect.commit()
    connect.close()

def add_login(password):
    connect = sqlite3.connect('login.db')
    cur = connect.cursor()
    cur.execute("INSERT INTO login VALUES (?)", (password,))
    connect.commit()
    connect.close()


def login():
    global count
    global begin
    count = '2'
    if dec == 'N':

        login_pass = input("Make a password for enter!")
        login_email = input("Type in an email!")
        create_new_login()
        create_new_email()
        add_login(login_pass)
        add_email(login_email)
        print("You made a new password!")
        count = '2'

    elif dec == 'Y':
        maybe = input("Type in password")
        connect = sqlite3.connect('login.db')
        cur = connect.cursor()
        check = cur.execute("SELECT rowid, * FROM login")
        for c in check:
            if maybe == c[1]:
                count = '2'
            elif maybe != c[1]:
                count = '22'

        connect.commit()
        connect.close()
    else:
        print("Please put a 'Y' or 'N' please!")

if __name__ == '__main__':
    #Aran was here
    #Xalan was here
    count = '2'
    dec = input("Do you have a login password? (Y/N)")
    begin = 0
    login()
    if len(count) == 2:
        print("WRONG!!")
    elif len(count) == 1:
        print("WELCOME TO PASSWORD SAVER!!")
        while begin==0:
            print("\n1. Show All Password")
            print("2. Show One Password")
            print("3. Add Password")
            print("4. Delete Password")
            print("5. Update Password")
            print("6. Delete Password Table")
            print("7. Change Login Password")
            print("8. Exit")
            print("Select an option......")
            option = input()
            if option == '1':
                PassEnd.display()


            elif option == '2':
                website = input("Which website do you want to look for?")
                PassEnd.one_look(website)
            elif option == '3':
                website = input("Type in your website:")
                email = input("Type in your email: ")
                user = input("Type in your username: ")
                password = input("Type in your password: ")
                PassEnd.add(website, email, user, password)
                PassEnd.check_dup()

            elif option == '4':
                PassEnd.display()
                id = input("Select ID to delete")
                PassEnd.delete(id)
                PassEnd.order()
            elif option == '5':
                # PassEnd.display()
                # id = input("Select the ID that you want to update")
                # email = input("Whats your new email?")
                # user = input("Whats your new username?")
                # password = input("Whats your new passsword?")
                # PassEnd.update(email, user, password, id)
                # print("UPDATED!")
                print("What do you want to update?: email, username, or password")
                choice = input()
                if choice == "email":
                    PassEnd.display()
                    id = input("Select ID to update")
                    new_email = input("what's your new email?")
                    PassEnd.email_update(new_email, id)
                    print("Email Updated!")
                elif choice == "username":
                    PassEnd.display()
                    id = input("Select ID to update")
                    new_user = input("what's your new username?")
                    PassEnd.user_update(new_user, id)
                    print("Username Updated!")
                elif choice == "password":
                    PassEnd.display()
                    id = input("Select ID to update")
                    new_password = input("what's your new password?")
                    PassEnd.password_update(new_password, id)
                    print("Password Updated!")


            elif option == '6':
                PassEnd.drop()
                PassEnd.create()
                print("All passwords deleted!")
            elif option == '7':
                try:
                    new_password = input("What is your new login password?")
                    new_email = input("Type in an email!")
                    send = Sender.sender(new_email)
                    deleteTable()
                    delete_Table()
                    create_new_login()
                    create_new_email()
                    add_login(new_password)
                    add_email(new_email)

                    print("New password changed!")
                except:
                    print("Password change not successful!")
            elif option == '8':
                break
            else:
                print("Not a Valid choice! Pick again!")
