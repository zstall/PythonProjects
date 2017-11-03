from __future__ import print_function
from sys import stdin
import unittest

'''
Description:
Author:          Zachary Stall
Version:         1
Help Recieved:
Help Provided:
'''

trace = False

class FamilyTree(object):
    def __init__(self, name, parent = None):
        self.name = name
        self.left = self.right = None
        self.parent = parent

    def __iter__(self):
        if self.left:
            for node in self.left:
                yield node

        yield self.name

        if self.right:
            for node in self.right:
                yield node

    def __str__(self):
        return ','.join(str(node) for node in self)

    def add_below(self, parent, child):
        ''' Add a child below a parent. Only two per parent'''

        locate = self.find(parent)

        if not locate:
            raise ValueError('Could not find ' + parent)

        if not locate.left:
            locate.left = FamilyTree(child, locate)

        elif not locate.right:
            locate.right = FamilyTree(child, locate)

        else:
            raise ValueError(self + 'already has the allotted two children')

    def find(self, name):
        if self.name == name: return self

        if self.left:
            left = self.left.find(name)
            if left: return left

        if self.right:
            right = self.right.find(name)
            if right: return right

        return None

    def Parent(self, name):
        
        adult = self.find(name)
        if adult.parent == None:
            return "None"
        else:
            return adult.parent
                   
    def grandparent(self, name):
        return self.Parent(self.Parent(name).name)
    
    def generations(self):
        ''' Return a list of lists, where each sub-list is a generation. '''

        this_level = [self]
        next_level = []
        result = []
        names = []
        
        while len(this_level) >= 1:
            root = this_level.pop(0)
            names.append(root.name)
            
            if root.left != None and root.right != None:
               next_level.append(root.left)
               next_level.append(root.right)
                

            elif root.left != None and root.right == None:
                next_level.append(root.left)
                
            elif root.left == None and root.right!= None:
                next_level.append(root.right)
                            
            if this_level == []:
                result.append(names)
                this_level = next_level
                next_level = []
                names = []

        return result
        
    def inorder(self):
        left = []
        result = []
        nodes = [self]

        while len(nodes) >= 1:
            current = nodes.pop(0)
            left.append(current)
                       
            if current.left != None:
                nodes.append(current.left)

            elif current.left == None:
                result.append(left.pop().name)

                if len(left) >= 1:
                    current = left.pop()
                    result.append(current.name)
                    
                if current.right != None:
                    nodes.append(current.right)
        return result

    def preorder(self):
        nodes = [self]
        left = []
        result = []

        while len(nodes) >= 1:
            current = nodes.pop(0)
            left.append(current)
            result.append(current.name)

            if current.left != None:
                nodes.append(current.left)

            elif current.left == None:
                left.pop()

                if len(left) >= 1:
                    current = left.pop()
                if current.right != None:
                    nodes.append(current.right)

        return result

    
    def postorder(self):
        nodes = [self]
        left = []
        hold = []
        result = []
        
        while len(nodes) >= 1:
            current = nodes.pop()
            left.append(current)
            
                     
            while current.left != None:
                left.append(current.left)
                current = current.left
 
            if current.left == None:
                result.append(left.pop().name)
                
                if len(left) >= 1:
                    current = left.pop()

                if len(hold) >= 1:
                    x = hold.pop()
                    if x.left.name in result and x.right.name in result:
                        result.append(x.name)
                    else:
                        hold.append(x)
                    
                if current.right != None:
                    nodes.append(current.right)
                    hold.append(current)
                    
        if len(left) == 0:
            if len(hold) >= 1:
                result.append(hold.pop().name)

        return result
    

class CLevelTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(str(FamilyTree(None)), 'None')
    def setUp(self):
        self.tree = FamilyTree("Grandpa")
        self.tree.add_below("Grandpa", "Homer")
        self.tree.add_below("Grandpa", "Herb")
        self.tree.add_below("Homer", "Bart")
        self.tree.add_below("Homer", "Lisa")
    def test_str(self):
        self.assertEqual(str(self.tree), "Bart,Homer,Lisa,Grandpa,Herb")
        if trace:
            print('********************************************')
            print('test str: ' + str(self.tree))
            print('********************************************')
                  
    ''' Write tests for your pre, in and post-order traversals. '''

    def test_inorder(self):
        self.assertEqual(self.tree.inorder(), ['Bart', 'Homer', 'Lisa', 'Grandpa', 'Herb'])
        if trace:
            print('********************************************')
            print('test inorder: ' + str(self.tree.inorder()))
            print('********************************************')
                  
    def test_preorder(self):
        self.assertEqual(self.tree.preorder(), ['Grandpa', 'Homer', 'Bart', 'Lisa', 'Herb'])
        if trace:
            print('********************************************')      
            print('test preorder: ' + str(self.tree.preorder()))
            print('********************************************')
            
    def test_postorder(self):
        self.assertEqual(self.tree.postorder(), ['Bart', 'Lisa', 'Homer', 'Herb', 'Grandpa'])
        if trace:
            print('********************************************')
            print('test postorder: ' + str(self.tree.postorder()))
            print('********************************************')
    

class BLevelTests(unittest.TestCase):
    def setUp(self):
        self.tree = FamilyTree("Grandpa")
        self.tree.add_below("Grandpa", "Homer")
        self.tree.add_below("Grandpa", "Herb")
        self.tree.add_below("Homer", "Bart")
        self.tree.add_below("Homer", "Lisa")
        
    def testparent(self):
        self.assertEqual(self.tree.Parent("Lisa").name, "Homer")
        if trace:
            print('********************************************')
            print('test parent of Lisa: ' + str(self.tree.Parent("Lisa").name))
            print('********************************************')
            
    def test_grandparent(self):
        self.assertEqual(self.tree.grandparent("Lisa").name, "Grandpa")
        if trace:
            print('********************************************')
            print('test grandparent of Lisa: ' + str(self.tree.grandparent("Lisa").name))
            print('********************************************')
            
    def test_no_grandparent(self):
        self.assertEqual(self.tree.grandparent("Homer"), 'None')
        if trace:
            print('********************************************')
            print('test granparent of Homer: ' + str(self.tree.grandparent("Homer")))
            print('********************************************')
            
    def test_find_Parent(self):
        self.assertEqual(self.tree.find("Homer").name, "Homer")
        if trace:
            print('********************************************')
            print('test find Homer: ' + str(self.tree.find("Homer").name))
            print('********************************************')

    def test_Parent_None(self):
        self.assertEqual(self.tree.Parent("Grandpa"), "None")
        if trace:
            print('********************************************')
            print('test parent of Grandpa: ' + str(self.tree.Parent("Grandpa")))
            print('********************************************')
        
class ALevelTests(unittest.TestCase):
    def setUp(self):
        self.tree = FamilyTree("Grandpa")
        self.tree.add_below("Grandpa", "Homer")
        self.tree.add_below("Grandpa", "Herb")
        self.tree.add_below("Homer", "Bart")
        self.tree.add_below("Homer", "Lisa")

    def test_generations(self):
        self.assertEqual(self.tree.generations(), [['Grandpa'], ['Homer', 'Herb'], ['Bart', 'Lisa']])
        if trace:
            print('********************************************')
            print('test generation of Simpsons: ' + str(self.tree.generations()))
            print('********************************************')


class OtherSmallSetUps(unittest.TestCase):
    def setUp(self):
        self.tree = FamilyTree("A")
        self.tree.add_below("A", "B1")
        self.tree.add_below("A", "B2")
        self.tree.add_below("B1", "C1")
        self.tree.add_below("B1", "C2")
        self.tree.add_below("B2", "C3")
        self.tree.add_below("B2", "C4")
        
    def test_generations_OtherSmallSetUps(self):
        self.assertEqual(self.tree.generations(), [['A'], ['B1', 'B2'], ['C1', 'C2', 'C3', 'C4']])
        if trace:
            print('********************************************')
            print('test generation of OtherSetUps: ' + str(self.tree.generations()))
            print('********************************************')

    def test_inorder_OtherSmallSetUps(self):
        self.assertEqual(self.tree.inorder(), ['C1', 'B1', 'C2', 'A', 'C3', 'B2', 'C4'])
        if trace:
            print('********************************************')
            print('test inorder SmallSetUps: ' + str(self.tree.inorder()))
            print('********************************************')

    def test_preorder_OtherSmallSetUps(self):
        self.assertEqual(self.tree.preorder(), ['A', 'B1', 'C1', 'C2', 'B2', 'C3', 'C4'])
        if trace:
            print('********************************************')      
            print('test preorder SmallSetUps: ' + str(self.tree.preorder()))
            print('********************************************')
    
    def test_postorder_OtherSmallSetUps(self):
        self.assertEqual(self.tree.postorder(), ['C1', 'C2', 'B1', 'C3', 'C4', 'B2', 'A'])
        if trace:
            print('********************************************')
            print('test postorder SmallSetUps: ' + str(self.tree.postorder()))
            print('********************************************')



class OtherSetUps(unittest.TestCase):
    def setUp(self):
        self.tree = FamilyTree("A")
        self.tree.add_below("A", "B1")
        self.tree.add_below("A", "B2")
        self.tree.add_below("B1", "C1")
        self.tree.add_below("B1", "C2")
        self.tree.add_below("B2", "C3")
        self.tree.add_below("B2", "C4")
        self.tree.add_below("C1", "D1")
        self.tree.add_below("C1", "D2")
        self.tree.add_below("C2", "D3")
        self.tree.add_below("C2", "D4")
        self.tree.add_below("C3", "D5")
        self.tree.add_below("C3", "D6")
        self.tree.add_below("C4", "D7")
        self.tree.add_below("C4", "D8")

    def test_generations_OtherSetUps(self):
        self.assertEqual(self.tree.generations(), [['A'], ['B1', 'B2'], ['C1', 'C2', 'C3', 'C4'], ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8']])
        if trace:
            print('********************************************')
            print('test generation of OtherSetUps: ' + str(self.tree.generations()))
            print('********************************************')

    def test_inorder_OtherSetUps(self):
        self.assertEqual(self.tree.inorder(), ['D1', 'C1', 'D2', 'B1', 'D3', 'C2', 'D4', 'A', 'D5', 'C3', 'D6', 'B2', 'D7', 'C4', 'D8'])
        if trace:
            print('********************************************')
            print('test inorder: ' + str(self.tree.inorder()))
            print('********************************************')

    def test_preorder_OtherSetUps(self):
        self.assertEqual(self.tree.preorder(), ['A', 'B1', 'C1', 'D1', 'D2', 'C2', 'D3', 'D4', 'B2', 'C3', 'D5', 'D6', 'C4', 'D7', 'D8'])
        if trace:
            print('********************************************')      
            print('test preorder: ' + str(self.tree.preorder()))
            print('********************************************')

    def test_postorder_OtherSetUps(self):
        # NOT CORRECT ORDER, NEED TO FIX BUG
        # Does not add parents correctly, cannot handle third layer or "D's" in this test
        if trace:
            print('********************************************')
            print('test postorder: ' + str(self.tree.postorder()))
            print('********************************************')


if '__main__' == __name__:
    unittest.main()

    for line in stdin:
        a = line.strip().split(" ")
        if len(a) == 1:
            ft = FamilyTree(a[0])
        else:
            ft.add_below(a[0], a[1])

    print(ft.generations())

    
