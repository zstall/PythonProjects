from __future__ import print_function
import unittest, sys

'''
Description: NQueens Problem: For a chess board with a given size (s x s), write a method
that can find where to place the same number as size queens so they cannot attack each other.

Author: Zachary Stall
Version: 1
Help Recieved: Dr. Beaty and Class!!!
Help Provided:
'''

'''
    Given the location of two queens, find if they are safe
    from each other.
'''

Trace = True
def safe(one, two):
    if one[0] == two[0]: return False
    if one[1] == two[1]: return False
    if abs(two[0]-one[0]) == abs(two[1]-one[1]): return False
    return True

def print_solution(size, placed):
    print("for:", size)
    if placed == []:
        print("no solution found")
        return

    print('-' * size)

    for i in range(size):
        for j in range(size):
            if [i, j] in placed:
                sys.stdout.write("Q")
            else:
                sys.stdout.write(".")
        print()

    print('-' * size)


def solve_queens(size, row, placed):

    if row == size:
        return placed
    
    for column in range(size):
        tmp = True
        for queen in placed:
            if not safe([row, column], queen):
                tmp = False
                break
        if tmp:
            foo = solve_queens(size, row+1, placed+[[row, column]])
            if foo:
                return foo
    return []

class TestSafePrintSolutions(unittest.TestCase):
    def test_unsafe(self):
        self.assertEqual(safe([0,0], [1,1]), False)
    def test_safe(self):
        self.assertEqual(safe([0,0], [1,2]), True)

    
    def test_print_unsafe(self):
        #visual tests if trace is true
        s1 = 2
        p1 = [[0,0], [1,1]]

        s2 = 4
        p2 = [[0,1], [1,3], [2,0], [3,2]]
        if Trace:
            print('-------------------------------------------------')
            print('Testing the print_solution method *NOT A SOLUTION*') 
            print_solution(s1, p1)
            print()
            print('-------------------------------------------------')
            print('Testing the print_solution method')
            print_solution(s2, p2)
        pass
    
class Test_solve_queens(unittest.TestCase):
    def test_solve_queens_NOSOLUTION(self):
        if Trace:
            print('Testing Solve Queens NO SOLUTIONS')
        # set size, 3 has no solutions  
        s = 3
        self.assertEqual(solve_queens(s, 0, []), [])
        solution =(solve_queens(s, 0, []))
        print_solution(s, solution)

    def test_solve_queens_4(self):
        if Trace:
            print('Testing solve for size 4x4')

        s = 4
        self.assertEqual(solve_queens(s, 0, []), [[0, 1], [1, 3], [2, 0], [3, 2]])
        solution =(solve_queens(s, 0, []))
        if Trace:
            print_solution(s, solution)

    def test_solve_queens_6(self):
        if Trace:
            print('Testing solve for size 6x6')

        s = 6
        self.assertEqual(solve_queens(s, 0, []), [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]])
        solution =(solve_queens(s, 0, []))
        if Trace:
            print_solution(s, solution)

    def test_solve_queens_8(self):
        if Trace:
            print('Testing solve for size 8x8')

        s = 8
        self.assertEqual(solve_queens(s, 0, []), [[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]])
        solution =(solve_queens(s, 0, []))
        if Trace:
            print_solution(s, solution)


if '__main__' == __name__:
    unittest.main()
