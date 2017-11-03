'''
Counting Characters

Chapter 5 Pg. 110

By Zachary Stall

This program will create a Dictionary with keys and values
and count the number of each unique character in a string.

'''

import pprint


message = 'Its the calm before the storm right here Wait, how was I gonna start this off? '

count = {}

for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
pprint.pprint(count)
