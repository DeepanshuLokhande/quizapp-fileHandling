from common import *
users = {}

def allUsers():
    with open("user.txt", "r") as file:
        for line in file:
            if line.strip().split(':') == ['']:
                continue
            else:
                userName, password = line.strip().split(':')
                users[userName] = password

def newUser(userName, password):
    with open("user.txt", "a") as file:  # Append mode to add new users
        file.write(f"{userName}:{password} \n")

def signUp(userName, password):
    if userName in users:
        print("User already exists")
    else:
        users[userName] = password
        print("User created successfully")
        newUser(userName, password)
        quiz()  # Call to quiz function

def logIn(userName, Password):
    if userName in users:
        if users[userName] == Password:
            print("Login successful")
            quiz()  # Call to quiz function
        else:
            print("Incorrect password")
    else:
        print("User does not exist")


allUsers()