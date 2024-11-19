from register import signUp, logIn

userdata = input('press 1 to sign up or 2 to login: ')
if userdata == '1':
    userName = input('Enter your username: ')
    password = input('Enter your password: ')
    signUp(userName, password)
elif userdata == '2':
    userName = input('Enter your username: ')
    password = input('Enter your password: ')
    logIn(userName, password)

