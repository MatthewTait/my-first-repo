
'''
This asks for the username and password
these will be stored as variables
'''

Username=input('Please enter your username: ')
Password=input('Please enter your password: ')

i=0
#Checks user name and password to check if they are correct
while True:
    if Username != 'Matthew123' and Password != '1234':
        print('Try again.')*1
        for i in range(0,3):
            if i == 3:
                break
                print('Out of tries.')
            else:
                continue
    else:
        print('You have access.')
        break
        
