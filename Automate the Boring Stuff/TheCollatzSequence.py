#! python3
'''
The Collatz Sequence

Chapter 3 Pg. 77

By Zachary Stall


This program asks the user to input a number and using the Collatz
Sequence will reduce the number to one. The program does this with a
collatz() method that if the number is even will //2, if the number is
odd then it will collatz() will return 3*number+1. It will recurse until
the number is one.

'''


print('Enter any integer number: ', end='') # Prompt user to input number (end='' allows user to put num on same line)

number = input()                            # Get input from user
try:
    num = int(number)                           # Convert number from string to an int
except ValueError:
    print('Error: Invalid Entry')
    print('Enter a new integer value: ', end='')
    num = int(input())
    
def collatz(n):                             # Collatz method
    
    while True:                             # Loop until n is 1
        if((n%2)==0):                       # Check in number is even
            n = n//2                        # If even int devide by 2
            print(n)                        # Print number
            if n == 1:                      # Check for end
                break

        else:
            n = 3*n+1                       # Check if negative
            print(n)                        # Print number
            if n == 1:                      # Check for end
                break

collatz(num)                                # Call method with number entered
