'''
Character Picture Grid

Chapter 4 Pg. 103

By Zachary Stall

This program takes a list named grid, and using while loops will rotate the
list 90 degrees.

'''

# Grid to rotate
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

i = 0                               # var to increment through "x" on list
j = 0                               # var to increment through "y" on list
maxx = len(grid)-1                  # get max value for x axis
maxy = len(grid[1])-1               # get max value for y axis

print()
while i <= maxx:                    # incrementing across x

    if j == (maxy + 1):             # Check for end of grid
        break
    
    while j <= maxy:                # increment through y
        print(grid[i][j], end='')   # print 90 degree rotated grid
        i+=1                        # increment
        
        if i == maxx:               # if x at max, move to next row
            j += 1
            i = 0
            print()                 # start next row

print()
            
                
    

