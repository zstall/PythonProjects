# CH 2 PG 41 If Statements, user name and password


print('Please enter your user name, or press return if you do not have a user name:')

enterUser = input()

while (enterUser == ''):
    print('Enter new user name: ')
    enterUser = input()


print('Please enter your password: ')

passWord = input()

print('You have created a user name and password.')
print('Please enter user name and password to get secret message.')

while True:
    print('User name: ')
    enterUser2 = input()
    if enterUser2 == enterUser:
        break
    
while True:
    print('Enter Password: ')
    passWord2 = input()
    if passWord2 == passWord:
        break

print('Success, you are a winner and now you have access.')
