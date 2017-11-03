from __future__ import print_function
import unittest
import math

'''
Description:     Creating a dictionary that will assign a value to a specific key and will use chaining.
                 Will also use hashing to assign key's and linear hashing for collisions

Author:          Zachary Stall

Version:         1

Help Provided:

Help Received:
'''

Trace = True

class dictionary:

    def __init__(self, init=None):

        self.__limit = 10
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0

        if init:
            for i in init:
                self.__setitem__(i[0], i[1])

    def __len__(self):
        if Trace:
            print('Number of key/values in dictionary: ' + str(self.__count))
        return self.__count

    def __flattened(self):
        return [item for inner in self.__items for item in inner]

    def __iter__(self):
        return(iter(self.__flattened()))

    def __str__(self):
        return(str(self.__flattened()))

    def __setitem__(self, key, value):
        ''' ADD to the dictionary. '''
        
        a = [key, value]
        location = abs(hash(key))%self.__limit

        if Trace:
            print('The hash location is:' + str(location))

        self.__items[location].append(a)
        self.__count += 1

        if Trace:
            print(self.__items)

                
    def __contains__(self, key):
        ''' Implements the 'in' operator. '''
        pass

    def hashvalue(self, key, size):
        return abs(hash(key))%size

    def nexthash(self, firsthash, size):
        return (firsthash+1)%size


''' C-level Work '''

class test_add_two(unittest.TestCase):

    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        self.assertEqual(len(s), 2)
        self.assertEqual(s[1], "one")
        self.assertEqual(s[2], "two")

        
               
    
    
if '__main__'==__name__:
    unittest.main()
