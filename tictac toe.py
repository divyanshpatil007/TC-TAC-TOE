#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We are going to make the game board using dictionary . 
    In which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

Gameboard= {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in Gameboard:
    board_keys.append(key)

'''  Now we have to print the updated Gameboard after every move in the game and 
    thus we  make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we will write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(Gameboard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if Gameboard[move] == ' ':
            Gameboard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if Gameboard['7'] == Gameboard['8'] == Gameboard['9'] != ' ': # across the top
                printBoard(Gameboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif Gameboard['4'] == Gameboard['5'] == Gameboard['6'] != ' ': # across the middle
                printBoard(Gameboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Gameboard['1'] == Gameboard['2'] == Gameboard['3'] != ' ': # across the bottom
                printBoard(Gameboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Gameboard['1'] == Gameboard['4'] == Gameboard['7'] != ' ': # down the left side
                printBoard(Gameboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Gameboard['2'] == Gameboard['5'] == Gameboard['8'] != ' ': # down the middle
                printBoard(Gameboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Gameboard['3'] == Gameboard['6'] == Gameboard['9'] != ' ': # down the right side
                printBoard(Gameboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif Gameboard['7'] == Gameboard['5'] == Gameboard['3'] != ' ': # diagonal
                printBoard(Gameboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Gameboard['1'] == Gameboard['5'] == Gameboard['9'] != ' ': # diagonal
                printBoard(Gameboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            Gameboard[key] = " "

        game()

if __name__ == "__main__":
    game()