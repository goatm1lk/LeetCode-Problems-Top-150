



from collections import deque
import random

#Problem:
# You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

# You start on square 1 of the board. In each move, starting from square curr, do the following:

# Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
# This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
# If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
# The game ends when you reach the square n2.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

# Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

# For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
# Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

def SnakesAndLadders(board):
    def faceValueToBoardValue(square,n):
        #To calculate the coordinates based on the Face Value, we can divide the square - 1 by n in order to get it's respective row. To get the column you can get the square - 1 modulo by n
        #The modulo will get the remainder when divided by n, so that will be the index for the column. However this only applies for even rows.
        #The boards Face Values will be alternating at each row, so in order to get the column index on odd rows we must alter the current column selected as the values are now descending so we use the equation n - 1 - c to calculate that. 
        #This will count starting at the index n - 1, and we will subtract from the current columns value in order to count to the new column with the correct Face Value.
        #I.E. [15,14,13,12,11], for 14 it would be [length = (5 - 1)] - [column index in ascending order = ((14 - 1) % 5)] == 4 - 3 = index 1, which is true since 14 is at index 1. 
        #We subtract 1 from square due to coordinates on the board are 0-indexed and the Face Values are 1 indexed.
        r = (square - 1) // n
        c = (square - 1) % n
        #Check if the row is an odd row.
        if r % 2 == 1:
            c = (n - 1) - c
        return [r,c]
    #Calculate the length of one array in the board n x n
    n = len(board)
    #We also want to reverse the board, as the board has 0 as the the last column.
    board.reverse()
    #Create a queue to hold the Face Counts of the board 1 through n * n
    q = deque()
    #Append the starting square and the amount of moves to the deque
    q.append([1,0])
    #Create a visit hash set so we cannot revist square's we have already rolled to.
    visit = set()
    
    #Loop through the queue to find the lowest amounts of dice rolls.
    while q:
        #Pop your current square and the amount of moves into variables.
        square, moves = q.popleft()
        
        #Now we would want to loop through the possible rolls we can get.
        for i in range(1,7):
            #We want to check the next square here with the dice roll.
            nextSquare = square + i
            # if the the next square has a ladder or a snake we would need to check the board value, in order to do that, we need the coordinates from the board that line up with its face value.
            r,c = faceValueToBoardValue(nextSquare,n)
            #If the board[r][c] is not equal to -1, then the nextSquare will be the destination of that snake or ladder.
            if board[r][c] != -1:
                nextSquare = board[r][c]
            #Check if the result is equal to the finish square
            if nextSquare == n * n:
                return moves + 1
            #Now add these results to the queue if none of those conditions pass, as we need check the rest of the posibilities.
            #We need to make sure haven't visited these values yet.
            if nextSquare not in visit:
                visit.add(nextSquare)
                q.append([nextSquare,moves + 1])
    #Return -1 if the q empties out without returning something first. This means no possible solutions to reach the goal.
    return -1

#Generate a board to use with n as it's length * width
def boardGenerator(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            decidingNum = random.randint(0,10)
            if decidingNum >= 8 and (i != n-1 and i != 0 and j != 0 and j != n-1):
                row.append(random.randint(1, n * n))
            else:
                row.append(-1)
        board.append(row)
    return board

board = boardGenerator(random.randint(2,6))
print(board)
print(SnakesAndLadders(board))
