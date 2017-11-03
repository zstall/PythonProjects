from __future__ import print_function
import unittest
import math
import copy

'''
Description:     Creating a dictionary that will assign a value to a specific key and will use
                 linear chaining for collisions. If the dictionary exceeds 78% load it will automatically
                 increase the dictionary size by double and rehash all values.
                 If the user knows that the dictionary is at less than 25% load they can halve the dicationary
                 size and rehash all the values.
                 

Author:          Zachary Stall

Version:         1

Help Provided:   None

Help Received:   None
'''

Trace = False


class dictionary:
    def __init__(self, init=None):

        self.__limit = 10
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0

        if init:
            for i in init:
                self.__setitem__(i[0], i[1])

    def __len__(self):
        return self.__count

    def __flattened(self):
        return [item for inner in self.__items for item in inner]

    def __iter__(self):
        return (iter(self.__flattened()))

    def __str__(self):
        return (str(self.__flattened()))
    
    def __setitem__(self, key, value):

        a = [key, value]
        ''' percentage must be less then 75% before rehashing '''
        high = .75
        low = .25
        percent = (self.__count / self.__limit)

        if percent <= high:
            
            location = abs(hash(key)) % self.__limit
                
            if len(self.__items[location]) == 0:
                self.__items[location].append(a)
                self.__count += 1

                return
            
            for item in self.__items[location]:
                if key == item[0]:
                    item[1] = value
                    return

                else:
                    self.__items[location].append(a)
                    self.__count += 1
                    return
                    
        if percent > high:
            self.__dblhash__(key, value)
            return

        ''' Trying to implement half hash automatically causes infinite recursion.
            Need to find a way to control when percentage is checked and halfing is done.
            For now, can only manually half hash table by calling method.
            
            if percent < low:

            self.__halfhash__(key, value)
            return
        '''

    def __getitem__(self, key):
            '''Returns a integer value '''

            location = abs(hash(key)) % self.__limit
            for item in self.__items[location]:
                if key == item[0]:
                    return item[1]
                else:
                    return

    def __contains__(self, key):
            ''' Returns a boolean value '''
            location = abs(hash(key)) % self.__limit
            for item in self.__items[location]:
                if key == item[0]:
                    return True
            return False


    ''' B - Level Work: Doubleing and Delete Item'''
    def __dblhash__(self, key, value):

        list_copy = copy.deepcopy(self.__items)

        del self.__items[:]

        self.__limit = self.__limit * 2
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0

        self.__setitem__(key, value)
        
        for item in list_copy:
            for i in item:
                self.__setitem__(i[0], i[1])
        return

    def __delitem__(self, key):
            location = abs(hash(key)) % self.__limit

            if self.__items[location] is None:
                return False

            for item in self.__items[location]:
                if key == item[0]:
                    self.__items[location] = []
                    self.__count -= 1
                    return True



    ''' A - Level Work: Halving, Keys, and Values'''    
    def __halfhash__(self):

        if (self.__count / self.__limit) >= .25:
            return

        else:

            list_copy = copy.deepcopy(self.__items)

            del self.__items[:]
            if self.__limit >= 1:
                self.__limit = self.__limit // 2
            self.__items = [[] for _ in range(self.__limit)]
            self.__count = 0

            for item in list_copy:
                for i in item:
                    self.__setitem__(i[0], i[1])
            

    def keys(self):

        print()
        print("*** Printing all keys ***")
        for item in self.__items:
            for i in item:
                print(i[0])
        return

    def values(self):

        print()
        print("*** Printing all values ***")
        for item in self.__items:
            for i in item:
                print(i[1])
        return



    ''' Extra Credit: Items'''
    def items(self):
        tmp = []
        print()
        print("*** Printing/Returning a list key, value pairs as 2-tuples ***")
        for item in self.__items:
            for i in item:
                tmp.append(i)
        print(tmp)
        return tmp

    def __eq__(dicta, dictb):

        a = dicta.items()
        b = dictb.items()

        if a == b:
            print()
            print("The dictionaries have the same key, value pairs. Result True.")
            return True
        else:
            print()
            print("The dictionaries do not have the same key, value pairs. Result False.")
            return False
    
    def print(self):
        if Trace:
            print()
            print('*******Start Dictionary*******')
            print(self.__items)
            print(self.__count)
            print('********End Dictionary********')
            print()
        else:
            pass

''' C-level Work '''

class test_add_two(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        self.assertEqual(len(s), 2)
        self.assertEqual(s[1], "one")
        self.assertEqual(s[2], "two")
        s.print()

class test_add_twice(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[1] = "one"
        self.assertEqual(len(s), 1)
        self.assertEqual(s[1], "one")
        s.print()

class test_store_false(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = False
        self.assertTrue(1 in s)
        self.assertFalse(s[1])
        s.print()
        
class test_store_none(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = None
        self.assertTrue(1 in s)
        self.assertEqual(s[1], None)
        s.print()
        
class test_none_key(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[None] = 1
        self.assertTrue(None in s)
        self.assertEqual(s[None], 1)
        s.print()
        
class test_False_key(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[False] = 1
        self.assertTrue(False in s)
        self.assertEqual(s[False], 1)
        s.print()
        
class test_collide(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[0] = "zero"
        s[10] = "ten"
        self.assertEqual(len(s), 2)
        self.assertTrue(0 in s)
        self.assertTrue(10 in s)
        s.print()

class test_hash(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s[5] = "five"
        s[6] = "six"
        s[12] = "twelve"
        s[13] = "thirteen"
        s[16] = "sixteen"
        self.assertEqual(len(s), 9)
        self.assertEqual(s[1], "one")
        self.assertEqual(s[2], "two")
        self.assertEqual(s[12], "twelve")
        s.print()

class test_delete(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s.__delitem__(2)
        s.print()

class test_halving(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        s.__halfhash__()
        s.print()

class test_deleting_halving(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "value one"
        s[2] = "delete me"
        s[3] = "value three"
        s.print()
        s.__delitem__(2)
        s.__halfhash__()
        s.print()

class test_hash_delete_halve(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "*one"
        s[2] = "*two"
        s[3] = "*three"
        s[4] = "*four"
        s[5] = "*five"
        s[6] = "*six"
        s[12] = "*twelve"
        s[13] = "*thirteen"
        s[16] = "*sixteen"
        
        s.__delitem__(1)
        s.__delitem__(3)
        s.__delitem__(4)
        s.__delitem__(6)
        s.__delitem__(13)
        s.__halfhash__()
        self.assertEqual(len(s), 4)
        self.assertEqual(s[5], "*five")
        self.assertEqual(s[2], "*two")
        self.assertEqual(s[16], "*sixteen")
        s.print()

class test_keys_values_items(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s[5] = "five"
        s.keys()
        s.values()
        s.items()

class test_eq_True(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"

        t = dictionary()
        t[1] = "one"
        t[2] = "two"
        t[3] = "three"

        self.assertEqual(s.__eq__(t), True)
        

class test_eq_False(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "threes"

        t = dictionary()
        t[1] = "one"
        t[2] = "two"
        t[3] = "three"

        self.assertEqual(s.__eq__(t), False)
        




if '__main__' == __name__:
    unittest.main()

