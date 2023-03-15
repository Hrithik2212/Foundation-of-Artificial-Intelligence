
player, opponent = 'x', 'o' 
  
def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] =='_'):
                return True
    return False 

def evaluate(b) : 
    
    # Checking for Rows  
    for row in range(3) :     
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :        
            if (b[row][0] == player) :
                return 1
            elif (b[row][0] == opponent) :
                return -1
  
    # Checking for Columns 
    for col in range(3) :
       
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
          
            if (b[0][col] == player) : 
                return 1
            elif (b[0][col] == opponent) :
                return -1
  
    # Checking for Diagonals 
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
      
        if (b[0][0] == player) :
            return 1
        elif (b[0][0] == opponent) :
            return -1
  
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
        if (b[1][1] == player ):
            return 1
        elif(b[1][1] == opponent):
            return -1
    
    return 0
    
def minimax(board , depth , isMax):
    hf = 0 
    score = evaluate(board)
    if (score==1):
        return (score , 1)
    elif (score==-1):
        return (score , -1) 
    if (isMovesLeft(board)==False):
        return (0 ,0)
        
    if(isMax):
        best = -1000
        for i in range(3):
            for j in range(3):
                if(board[i][j]=='_'):
                    board[i][j] = opponent 
                    hf += evaluate(board)
                    board[i][j] = player 
                    hf += evaluate(board)
                    best = max(best , minimax(board , depth+1 , not isMax)[0] )
                    board[i][j] ='_'
        return (best , hf)
        
    else :
        best = 1000
        for i in range(3):
            for j in range(3):
                if(board[i][j]=='_'):
                    board[i][j] = player 
                    hf += evaluate(board)
                    board[i][j] = opponent
                    hf += evaluate(board)
                    best = min(best , minimax(board , depth +1 , not isMax )[0])
                    board[i][j] = '_'
        return (best , hf)
        
def findbestMove(board):
    bestVal = -1000 
    bestMove = (-1, -1)
    
    for i in range(3):
        for j in range(3) :
            if (board[i][j] == '_'):
                board[i][j] = player 
                moveVal , hf  = minimax(board , 0 , False)
                board[i][j] = '_'
                if (moveVal > bestVal) :
                    bestMove = (i,j)
                    bestVal = moveVal
    print("The value of best move is :",bestVal)
    print()
    return bestMove , hf 
    

board = [
    ['x','o','x'],
    ['o','o','x'],
    ['_','_','_']
    ]
    
bestMove , hf= findbestMove(board)

print("The optimal move is:")
print(f"ROW {bestMove[0]} , COLUMN {bestMove[1]}")
print("The Score of the heursitic function is ",hf )



"""
OUTPUT

The best move is : 1

The optimal move is:
ROW 2 , COLUMN 2
The Score of the heursitic function is  1
"""
