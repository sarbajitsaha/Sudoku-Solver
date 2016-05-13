import sys
import time

#sys.stdin=
file = open("sudoku_problem.txt","r")
sys.setrecursionlimit(10000000)

count = 0

"""
   check if the number is in the 3X3 sub matrix already
"""
def checkSubMatrix(matrix,row,col,num):
    for i in xrange(3):
        for j in xrange(3):
            if(matrix[row+i][col+j]==num):
                return False
    return True


"""
   check if the number is in the row already
"""
def checkRow(matrix,row,num):
    for i in xrange(9):
        if(matrix[row][i]==num):
            return False
    return True

"""
   check if the number is in the column already
"""
def checkCol(matrix,col,num):
    for i in xrange(9):
        if(matrix[i][col]==num):
            return False
    return True


"""
   check if all the conditions satisfy
"""
def checkAll(matrix,row,col,num):
    if (checkRow(matrix,row,num))==False or (checkCol(matrix,col,num))==False or (checkSubMatrix(matrix,row - row%3,col - col%3,num))==False:
        return False
    return True

"""
   check if any blank space remains
"""
def checkBlank(matrix):
    for i in xrange(9):
        for j in xrange(9):
            if(matrix[i][j]==0):
                return False
    return True

"""
   Main function to solve matrix with recursive backtrack
"""
def solveMatrix(matrix):
    global count
    
    #solution found
    if(checkBlank(matrix))==True:
        return True 

    """
       find the coordinates of blank space
    """
    check = True
    for i in xrange(9):
        for j in xrange(9):
            if(matrix[i][j]==0):
                a=i
                b=j
                check = False
                break
        if (check==False):
            break
    
    for num in xrange(1,10):
        if(checkAll(matrix,a,b,num))==True: #possible solution
            count+=1 #no of iterations
            #print a,b,num
            matrix[a][b] = num #set value
            if(solveMatrix(matrix))==True: #calling recursively
                return True #solved
            matrix[a][b] = 0 #unset value in case wrong

    return False 

"""
  function to print the solved matrix
"""
def printMatrix(matrix):
    for i in xrange (9):
        for j in xrange(9):
            print matrix[i][j],
        print "\n",


if __name__=="__main__":
    print 'Create a file called "sudoku_problem.txt"(without quotes) and input the sudoku matrix'
    print 'Enter 0 for blank spaces and each number should be separated by a space and each row by a newline'
    print 'Check the example included\n\n'
    
    matrix = [0 for i in xrange(9)]
    for i in xrange(0,9):
        matrix[i] = map(int,file.readline().strip().split(" "))

    start = time.time()
    if(solveMatrix(matrix))==True:
        print "No of iterations : ",count
        print "Solution found\n"
        printMatrix(matrix)
    else:
        print "No of iterations : ",count
        print "No solution found"
    stop = time.time()
    print "Time taken : %f sec"%(stop-start)
    raw_input()
        


