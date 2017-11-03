from __future__ import print_function
import unittest

'''
Description: findandreplace is a method the recursively searches for a char/element,
             then if found will replace that char/element with another designated
             char/element.
                    
Author: Zachary Stall
Version: 1
Help Received: None
Help Provided: None
'''

trace = False

def findandreplace(find, replace, string):
    result = type(string)()

    # Test string, find, and replace are the same type, if lists:
    if type(string) == list and type(find) != list and find != None:
        find = [find]
    if type(string) == list and type(replace) != list and replace != None:
        replace = [replace]

    if find == None or len(find) < 1:               # Get the length of what you are looking for
        a = 1                                       # If the what your looking for is NONE
    else:                                           # Set length of a to one to avoid error
        a = len(find)
    
    if string == result:                            # Check to see if recursed over entire string
        return(result)                              # Return completed result

    if find == string[:a]:                          # Check if a part of string matches find
        if replace == None:                         # If replace is NONE, do not change string
            replace = find
        result += replace + findandreplace(find, replace, string[a:]) # Add replaced character to result and recurse

    else:
        result += string[:a] + findandreplace(find, replace, string[a:]) # If no match, add existing sting element and recurse

    return result

def results_console(f, r, s, res):
    if trace:
        if f == "":
            f = "delete space"
        elif f == " ":
            f = "space"
            
        if r == "":
            r = "delete space"
        elif r == " ":
            r = "space"
            
        print("**************************************************************")
        print("Find: " + str(f) + "  Replace: " + str(r) + "  String: " + str(s))
        print("Result: " + str(res))
        print("****************************************************************")

class TestFindAndReplace(unittest.TestCase):
    def test_all_none(self):
        self.assertEqual(findandreplace(None, None, None), None)
        results_console(None, None, None, findandreplace(None, None, None))
        
    def test_find_none(self):
        self.assertEqual(findandreplace(None, "a", "aabb"), "aabb")
        results_console(None, "a", "aabb", findandreplace(None, "a", "aabb"))

    def test_find_empty(self):
        self.assertEqual(findandreplace("", "a", "aabb"), "aabb")
        results_console("", "a", "aabb", findandreplace("", "a", "aabb"))

    def test_replace_none(self):
        self.assertEqual(findandreplace("a", None, "aabb"), "aabb")
        results_console("a", None, "aabb", findandreplace("a", None, "aabb"))

    def test_string_none(self):
        self.assertEqual(findandreplace("a", "b", None), None)
        results_console("a", "b", None, findandreplace("a", "b", None))
        
    def test_simple(self):
        self.assertEqual(findandreplace("a", "b", "aabb"), "bbbb")
        results_console("a", "b", "aabb", findandreplace("a", "b", "aabb"))

    def test_remove(self):
        self.assertEqual(findandreplace(" ", "", " a abb"), "aabb")
        results_console(" ", "", " a abb", findandreplace(" ", "", " a abb"))

    def test_last(self):
        self.assertEqual(findandreplace("z", "y", "aabz"), "aaby")
        results_console("z", "y", "aabz", findandreplace("z", "y", "aabz"))
                
    def test_middle(self):
        self.assertEqual(findandreplace("z", "y", "aazb"), "aayb")
        results_console("z", "y", "aazb", findandreplace("z", "y", "aazb"))

    def test_list(self):
        self.assertEqual(findandreplace([1], [5], [1, 2, 3]), [5, 2, 3])
        results_console([1], [5], [1, 2, 3], findandreplace([1], [5], [1, 2, 3]))

    def test_list_middle(self):
        self.assertEqual(findandreplace([2], [5], [1, 2, 3]), [1, 5, 3,])
        results_console([2], [5], [1, 2, 3], findandreplace([2], [5], [1, 2, 3]))

    def test_list_last(self):
        self.assertEqual(findandreplace([3], [5], [1, 2, 3]), [1, 2, 5])
        results_console([3], [5], [1, 2, 3], findandreplace([3], [5], [1, 2, 3]))

    def test_list_find_none(self):
        self.assertEqual(findandreplace(None, [5], [1, 2, 3]), [1, 2, 3])
        results_console(None, [5], [1, 2, 3], findandreplace(None, [5], [1, 2, 3]))

    def test_list_replace_none(self):
        self.assertEqual(findandreplace([1], None, [1, 2, 3]), [1, 2, 3])
        results_console([1], None, [1, 2, 3], findandreplace([1], None, [1, 2, 3]))

    def test_list_replace_empty(self):
        self.assertEqual(findandreplace([""], [1], ["", 2, 3]), [1, 2, 3])
        results_console([""], [1], ["", 2, 3], findandreplace([""], [1], ["", 2, 3]))

    def test_list_remove(self):
        self.assertEqual(findandreplace([1], [], [1, 2, 3]), [2, 3])
        results_console([1], [], [1, 2, 3], findandreplace([1], [], [1, 2, 3]))

    
    def test_list_winteger(self):
        self.assertEqual(findandreplace(1, 5, [1, 2, 3]), [5, 2, 3])
        results_console(1, 5, [1, 2, 3], findandreplace(1, 5, [1, 2, 3]))
    
        
    def test_gettysburg(self):
        self.assertEqual(findandreplace("Four score", "Twenty", "Four score and seven years ago"), "Twenty and seven years ago")
        results_console("Four score", "Twenty", "Four score and seven years ago", findandreplace("Four score", "Twenty", "Four score and seven years ago"))
        
if '__main__' == __name__:
    unittest.main()

    
    
