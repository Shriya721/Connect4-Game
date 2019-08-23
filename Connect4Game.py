###########################################################
    #  Computer Project #7
    #
    #  Algorithm
    #    displays connect 4 logo and description of how to play the game
    #    user is asked to pick a color (either black or white)
    #    if wrong color is inputed then user is reprompted to enter either black or white 
    #       assigns color picked to player who inputed color (black or white) and assigns other color to opponent (either black or white)
    #       displays empty board with blank squares
    #       prompts player 1 to input a column to where to drop the piece (piece is dropped on the bottom row)
    #       then prompts player 2 to input a column to drop a piece
    #       if player enters a wrong column then reprompts to enter between 1 and 7
    #       if column is full prompts user to pick another column
    #       game continues until there is a four in a row or a draw (entire board is full)
    #       players can enter pass and by default other player wins
    #       players can also exit and game exits prompting thank you message (no one wins)
    #    asks players if they want to play again and if yes then goes through entire game otherwise prompts thank you message and exits program
    ###########################################################
pieces = {'black':'b', 'white':'w'}
COLUMN = 7
ROW = 6


def initialize():
    '''
    function sets each element in the board to 0
    initializes all the element in a 6 by 7 board to 0 indicating no disc
    returns the initialed board 
    '''
    board = [[],[],[],[],[],[]] #creates an empty list for rows and columns 
    for i in range(ROW):
        board [i]= [0] *COLUMN  #initializes everything in a row and column to 0 
    return board #returns the initialized board

def choose_color():
    '''
    player inputs a color
    function checks whether the color is white or black 
    assigns the color picked by the player to the player and other color to the opponent
    if a color that's not black or white is entered then player reprompted to enter black or white
    returns a statement with color assignment 
    '''
    user_color = input("Pick a color: ") #player picks color 
    user_color_lower = user_color.lower()
    while True:
        if (user_color_lower =='white'): 
            #assigns player 1 white and opponent black
            print ( "You are '{}' and your opponent is 'black'.".format(user_color_lower)) 
            return user_color_lower #returns statement indicating color assignment 
            break
        elif(user_color_lower == 'black'):
            #assigns player 1 black and opponent white
            print( "You are '{}' and your opponent is 'white'.".format(user_color_lower))
            return user_color_lower #returns statement indicating color assignment 
            break
        else:
            #prompts player if incorrect color is entered
            print("Wrong color; enter only 'black' or 'white', try again.") 
            user_color = input("Pick a color: ") #asks player to enter black or white 
            user_color_lower = user_color.lower()
    
            

def board_display(board):
    '''
    board: the initialized board with 0's as all the elements 
    function creates the image of the board displayed to play the game
    returns nothing but prints current board  
    '''
    print("Current board:") 
    C = COLUMN
    R = ROW
    #creates the image of the game board 
    hline = '\n' + (' ' * 2) + ('+---' * C) + '+' + '\n'
    numline = ' '.join([(' ' + str(i) + ' ') \
                        for i in range(1, C + 1)])
    str_ = (' ' * 3) + numline + hline
    for r in range(0, R): 
        str_ += str(r+1) + ' |'
        for c in range(0, C):
            str_ += ' ' + \
                (str(board[r][c]) \
                     if board[r][c] is not 0 else ' ') + ' |'
        str_ += hline
    print (str_)


def drop_disc(board, column, color): 
    '''
    board: the initialized board with 0's as all the elements
    column: integer column that is inputed by the user
    color: the color that was picked my the player
    function drops the disc in the board created by the board display function
    based on which players turn it is (player 1 or 2) function drops that color piece ('b' or'w') in the designated space
    returns row number if valid column is entered and column is not full 
    returns 'full' if column is full
    returns None is column is invalid
    '''
    #assigns color to disc based on what the player has chosen 
    if (color == 'white'): 
        color = 'w'
    else:
        color = 'b'
    if (0<column and column<8): #column can only be between 1 to 7
       
        column -=1
        for element in range (ROW-1,-1,-1): #starts from the lowest row and goes up (bottom of columns) 
            if(element == 0 and board[element][column] != 0): #if the top most row and the element in that spot is nonzero
                print("This column is full. Please try again.") #column is full 
                return "full" #returns full 
                break
                
                
            elif(board[element][column] == 0): #if element is zeor then drop colored disc in square
                board[element][column] = color
                board_display(board)
                return element+1
                break
               
            else:
                continue #any other case just continue game     
               
    else:
        #player is prompted to enter again if invalid column and function returns None
        print("Invalid column: 1 <= column <= 7. Please try again.") 
        return None

        
def check_disc(board, row, column):
    '''
    board: current board of the game
    row: row that is returned by the drop_disc function
    column: the number the player inputs during their turn
    function checks if column and row are 0 if they are then return None because space does not have disc
    function checks for horizontal win creating a tuple of columns and comparing around them in a row
    function checks for vertical win creating a tuple of rows and comparing around them in a column
    function checks for positive diagonals creating a tuple of row and columns
    function checks for negative diagonals creating a tuple of row and columns
    returns True if there is a horizontal, vertical or positive or negative diagonal win
    returns False if there is no win
    '''

    four_in_row = False #set to False (indicating no win)
    
    if(board[row-1][column-1]==0):
        return four_in_row
    if ((column) ==0 or (row) ==0): #if column or row is still initialied to 0
        #returns None because no win yet
        return None 

    for the_column in range(COLUMN-3): #checks for horizontal win 
        disc_column= [the_column,the_column+1,the_column+2,the_column+3]
        disc_column_tuple = (disc_column) #creates a tuple of columns
        #checks all the elements horizontally around the specific disc 
        if(board[row-1][the_column+3] == board[row-1][the_column+2] == board[row-1][the_column+1] == board[row-1][the_column]):
            for index in range(len(disc_column_tuple)): #runs through entire length of tuple
                #compares elements of tuple at specific index to the column - 1
                if disc_column_tuple[index] == (column-1):
                    four_in_row = True 
                    return four_in_row #returns True if four in a row

    
 
    for the_row in range(ROW-3): #checks for vertical win 
        disc_row = [the_row,the_row+1,the_row+2,the_row+3]
        disc_row_tuple = (disc_row) #creates of tuple of rows
        #checks all the elements vertically around the specified disc 
        if(board[the_row+3][column-1] == board[the_row+2][column-1] == board[the_row+1][column-1] == board[the_row][column-1]):
            for index in range(len(disc_row_tuple)): #runs through entire length of tuple
                #compares elements of tuple at specific index to row - 1
                if disc_row_tuple[index] == (row-1):
                    four_in_row = True
                    return four_in_row #returns True if four in a row 
    
    for a_row in range(ROW-3): #checks for positive diagonal win (checks both rows and columns)
        for a_column in range(COLUMN-3):
#            disc_row_diag = [a_row, a_row+1,a_row+2,a_row+3]
#            disc_row_diag_tuple = (disc_row_diag)
#            disc_col_diag = [a_column, a_column+1,a_column+2,a_column+3]
#            disc_col_diag_tuple = (disc_col_diag)
            #creates a tuple with row and column 
            postive_diag_tuple= ([a_row,a_column], [a_row +1, a_column+1], [a_row +2, a_column+2], [a_row +3, a_column+3])
            #checks all the elements in a positive diag around the specified disc
            if (board[a_row+3][a_column+3] == board[a_row+2][a_column+2] == board[a_row+1][a_column+1] == board[a_row][a_column]):
                for index in range(len(postive_diag_tuple)): #runs through entire length of tuple
                    #compares elements of tuple at specific index to row - 1 and column - 1
                    if postive_diag_tuple[index] == [(row-1),(column-1)]:
                        four_in_row = True
                        return four_in_row #returns True if four in a row 
                       
    for a_row1 in range(ROW-3): #checks for negative diagonal win (checks both rows and columns)
        for a_column1 in range(3,COLUMN):
#            disc_row_diag1 = [a_row1, a_row1+1,a_row1+2,a_row1+3]
#            disc_row_diag_tuple1 = (disc_row_diag1)
#            disc_col_diag1 = [a_column1, a_column1-1,a_column1-2,a_column1-3]
#            disc_col_diag_tuple1 = (disc_col_diag1)
            #creates a tuple with row and column
            negative_diag_tuple = ([a_row1,a_column1], [a_row1 +1, a_column1-1], [a_row1 +2, a_column1-2], [a_row1 +3, a_column1-3])
            #checks all the elements in a negative diag around the specified disc
            if (board[a_row1+3][a_column1-3] == board[a_row1+2][a_column1-2] == board[a_row1+1][a_column1-1] == board[a_row1][a_column1]):
                for index in range (len(negative_diag_tuple)): #runs through entire length of tuple
                    #compares elements of tuple at specified index to row - 1 and column - 1
                    if negative_diag_tuple[index] == [(row-1),(column-1)]:
                        four_in_row = True
                        return four_in_row #returns True if four in a row 
    return four_in_row #returns False if no four in a row 
    
  
            
def is_game_over(board):
    
    '''
    board: current board of the game
    calls the check_disc function to see if there is a four in a row or not
    if there is a four in a row for white then returns the color white
    if there is a four in a row for black then returns the color black
    in order for it to be a draw there cannot be a four in a row and all the elements are full meaning none of them equals 0
    if there is no draw nor four in a row then function returns None 
    
    '''
    
    for column in range (1,COLUMN+1):
        for row in range(1,COLUMN):
            four_in_row = check_disc(board,row,column) #calls check_disc function to determine whether or not four in a row
            
            if (four_in_row == True):
                if (board[row-1][column-1] == 'w'): 
                    return 'white' #if white wins then returns the color white 
                    break
                else:
                    return 'black' #if black wins then returns the color black 
                    break
            else:
                continue
    for col in range(1,COLUMN+1):   
        #if check_disc is False and the element is not equal to 0 then there is a draw
        if (board[0][col]!=0 and four_in_row == False):
            return 'draw'
            break
        else:
            return None #there is no win nor draw so returns None 
       
   
             
          

                

def main():
    '''
    function displays logo of Connect 4 and the description of of how to play game
    function asks player to pick a color and assigns other color to opponent
    displays initialized empty board to start game
    asks player 1 to input a column number and function drops disc in that specified column
    then asks player 2 to input a column numebr and drops disc in that colum 
    if incorrect column number player is prompted again to enter a column number again
    if column is full then player is prompted to enter a column number again
    if invalid input then player is prompted with the options of valid inputs to input valid statement
    players keep playing game until player enters pass where other player who didn't enter pass wins
    if player enters exit entire program ends with thank you message displayed
    otherwise players keep playing until one player wins
    after player wins or enters pass then prompted to keep playing or not
    if player picks yes then game starts over and if not then program stops with thank you message is displayed
    '''
    #connect 4 logo and game description 
    banner = """
       ____ ___  _   _ _   _ _____ ____ _____ _  _   
      / ___/ _ \| \ | | \ | | ____/ ___|_   _| || |  
     | |  | | | |  \| |  \| |  _|| |     | | | || |_ 
     | |__| |_| | |\  | |\  | |__| |___  | | |__   _|
      \____\___/|_| \_|_| \_|_____\____| |_|    |_|  
    """
    intro = """
    Connect Four is a two-player connection game in which the players first choose a color and \
    then take turns dropping one colored disc from the top into a seven-column, six-row vertically suspended grid. \
    The pieces fall straight down, occupying the lowest available space within the column. \
    The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs. 
    """
    usage = """
        Usage:
            pass:   give up, admit defeat
            exit:   exit the game
            i:      drop a disk into column i
    """
    print(banner)
    print(intro)
    print(usage)
     
    continue_game = 'yes'  # can't use "continue" because it has a special meaning
    while continue_game == 'yes':
        initial_board = initialize() #calls initial board function 
        color =choose_color() #calls color function to assign color 
        board_display(initial_board) #displays initial board (empty)
        while True:
            if color == 'black': #assigns color chosen to player 1
                color_opponent = 'white' #assigns other color to player 2
            else:
                color_opponent = 'black' 
        
            user_choice = input("{}'s turn :> ".format(color)) #gets user input for player 1
            user_choice_lower = user_choice.lower()
            if (user_choice.isdigit() == True): #checks if column is a digit 
         
                #calls drop_disc with column user enters and color chosen to update initial board 
                disc = drop_disc (initial_board,int(user_choice),color) 
           
               
                if (disc == None or disc == 'full'):#executes if drop_disc returns None or Full
                    #
                    user_choice = input("{}'s turn :> ".format(color)) #asks for user input 
                    user_choice_lower = user_choice.lower()
                    if (user_choice.isdigit() == True): #does the same thing and checks if input is a digit
                        disc = drop_disc (initial_board,int(user_choice),color) #calls drop_disc
                        four_in_row = check_disc(initial_board, disc, int(user_choice)) #calls check_disc to check for a win 
                        if (four_in_row == True):
                            print (is_game_over(initial_board), " wins!") #if win calls is_game_over to print color that won 
                            break
                    elif(user_choice_lower == 'pass'): #if pass is entered then other player wins by default 
                        print ("{} gave up! {} is the winner!! yay!!!".format(color,color_opponent))
                        break
                    elif(user_choice_lower == 'exit'): #if exit then program exits and prints thank you message 
                        print("\nThanks for playing! See you again soon!")
                        break
                #checks for four in a row and prints it for specified color      
                four_in_row = check_disc(initial_board, disc, int(user_choice))
                
                if (four_in_row == True):
                    print (is_game_over(initial_board), " wins!")
                    break
            elif(user_choice_lower == 'pass'): #if pass is entered then other player wins by default 
                print ("{} gave up! {} is the winner!! yay!!!".format(color,color_opponent))
                break
            elif(user_choice_lower == 'exit'):#if exit then program exits and prints thank you message
                print("\nThanks for playing! See you again soon!")
                break
             
            else:
                print("Invalid option") #Invalid option if player enters something not specified
                print()
                print(usage)
                user_choice = input("{}'s turn :> ".format(color)) #asks user to input again 
                user_choice_lower = user_choice.lower()
                #asks user to input and do the same thing again where it gets column number calls drop_disc
               
                if (user_choice.isdigit() == True):
                    
                    disc = drop_disc (initial_board,int(user_choice),color)
                    
                    
                    if (disc == None or disc == 'full'): #checks to see if None or full 
                        
                        user_choice = input("{}'s turn :> ".format(color))
                        user_choice_lower = user_choice.lower()
                        if (user_choice.isdigit() == True):
                            disc = drop_disc (initial_board,int(user_choice),color)
                            four_in_row = check_disc(initial_board, disc, int(user_choice))
                            if (four_in_row == True):
                                print (is_game_over(initial_board), " wins!")
                                break
                    elif(user_choice_lower == 'pass'): #if pass is entered then other player wins by default 
                        print ("{} gave up! {} is the winner!! yay!!!".format(color,color_opponent))
                        break
                    elif(user_choice_lower == 'exit'):#if exit then program exits and prints thank you message
                        print("\nThanks for playing! See you again soon!")
                        break
                    #checks and prints if four in a row   
                    four_in_row = check_disc(initial_board, disc, int(user_choice))
                    if (four_in_row == True):
                        print (is_game_over(initial_board), " wins!")
                        break
                elif(user_choice_lower == 'pass'): #if pass is entered then other player wins by default 
                    print ("{} gave up! {} is the winner!! yay!!!".format(color,color_opponent))
                    break
                elif(user_choice_lower == 'exit'):#if exit then program exits and prints thank you message 
                    print("\nThanks for playing! See you again soon!")
                    break
                   
           # while loop is for opponents color and does the same thing as for the player 1's color (too much commenting because basically the same comment)
            user_choice = input("{}'s turn :> ".format(color_opponent))
            user_choice_lower = user_choice.lower()
            if (user_choice.isdigit() == True):
         
                
                disc = drop_disc (initial_board,int(user_choice),color_opponent)
                
               
                if (disc == None or disc == 'full'):
                    
                    user_choice = input("{}'s turn :> ".format(color_opponent))
                    user_choice_lower = user_choice.lower()
                    if (user_choice.isdigit() == True):
                        disc = drop_disc (initial_board,int(user_choice),color_opponent)
                        four_in_row = check_disc(initial_board, disc, int(user_choice))
                        if (four_in_row == True):
                            print (is_game_over(initial_board), " wins!")
                            break
                    elif(user_choice_lower == 'pass'):
                        print ("{} gave up! {} is the winner!! yay!!!".format(color_opponent,color))
                        break
                    elif(user_choice_lower == 'exit'):  
                        print("\nThanks for playing! See you again soon!")
                        break
                     
                four_in_row = check_disc(initial_board, disc, int(user_choice))
                if (four_in_row == True):
                    print (is_game_over(initial_board), " wins!")
                    break
            elif(user_choice_lower == 'pass'):
                print ("{} gave up! {} is the winner!! yay!!!".format(color_opponent,color))
                break
            elif(user_choice_lower == 'exit'):
                 print("\nThanks for playing! See you again soon!")
                 break
                 
            else:
                print("Invalid option")
                print()
                print(usage)
                user_choice = input("{}'s turn :> ".format(color_opponent))
                user_choice_lower = user_choice.lower()
                if (user_choice.isdigit() == True):
         
                
                    disc = drop_disc (initial_board,int(user_choice),color_opponent)
                    
                    if (disc == None or disc == 'full'):
                    
                        user_choice = input("{}'s turn :> ".format(color_opponent))
                        user_choice_lower = user_choice.lower()
                        if (user_choice.isdigit() == True):
                            disc = drop_disc (initial_board,int(user_choice),color_opponent)
                            four_in_row = check_disc(initial_board, disc, int(user_choice))
                            if (four_in_row == True):
                                print (is_game_over(initial_board), " wins!")
                                break
                            elif(user_choice_lower == 'pass'):
                                print ("{} gave up! {} is the winner!! yay!!!".format(color_opponent,color))
                                break
                            elif(user_choice_lower == 'exit'):  
                                 print("\nThanks for playing! See you again soon!")
                                 break
                                 
                    four_in_row = check_disc(initial_board, disc, int(user_choice))
                    if (four_in_row == True):
                        print (is_game_over(initial_board), " wins!")
                        break
                elif(user_choice_lower == 'pass'):
                    print ("{} gave up! {} is the winner!! yay!!!".format(color_opponent,color))
                    break
                elif(user_choice_lower == 'exit'):
                    print("\nThanks for playing! See you again soon!")
                    break
                   
                
          
        #if statement in order to exit the outer while loop when player enters exit and displays thank you message   
        if (user_choice_lower == 'exit'):
            break
        #if yes is entered goes through a new game but if no is entered then displays thank you message and ends program 
        continue_game = input("Would you like to play again? ").lower()
        
           
    else:
        print("\nThanks for playing! See you again soon!")
    
if __name__ == "__main__":
    main()

