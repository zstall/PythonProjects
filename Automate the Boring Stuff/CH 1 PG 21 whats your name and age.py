# CH 1 PG 21 What's your name and age

print('Hello, what is you name?')
myName = input()    # Get the users name

print('It is good to meet you ' + myName)
print('The length of your name is: ')
print(len(myName))

print('How old are you ' + myName + ': ')
myAge = input()     # Get the users age

print(myName + ', next year you will be ' + str(int(myAge) + 1 ))

