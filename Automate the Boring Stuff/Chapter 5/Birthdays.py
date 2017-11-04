'''
Birthday Program

Chapter 5 Pg. 107

This program displays the birthdays of anyone in the dictionary.
It also allows you to store new birthdays, however it loses the
data when the file is quit. In chapter 8 we learn how to store data
on the hard drive.
'''

birthdays = {'Caitlin': 'Feb 12', 'Zach': 'March 3'}


while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the bithday of ' + name)
    else:
        try:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            dbay = input()
            birthdays[name] = bday
            print('Birthday database updated.')
        except NameError:
            print('Error: Cannot leave blank')
            print('Enter a birthdate: ', end='')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')
        
