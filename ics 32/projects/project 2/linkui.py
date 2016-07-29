# Solomon Chan 40786337 and Tiancheng Xu 74436321. ICS 32 LAB 7 FUNCTIONS FOR BOTH USER INTERFACE

import collections
import connectfour

ConnectFourGameState = collections.namedtuple('ConnectFourGameState', ['board', 'turn'])

BOARD_COLUMNS = 7
BOARD_ROWS = 6

NONE = ' '
RED = 'R'
YELLOW = 'Y'





def _option_d(game_state:ConnectFourGameState,col:int)->ConnectFourGameState:
    try:
        game_temp = drop_option(game_state,col)
        _rotate_board(game_temp)
        return game_temp
    except:
        print('Unsucessful')
        return game_state


def _option_p(game_state:ConnectFourGameState,col:int)->ConnectFourGameState:
    try:
        game_temp = pop_option(game_state,col)
        _rotate_board(game_temp)
        return game_temp
    except:
        print('Unsucessful')
        return game_state



        


                    
def drop_option(game_state:ConnectFourGameState,col:int)-> ConnectFourGameState:
    '''if user chooses d, drop the piece'''

    try:
        
        game_state = connectfour.drop_piece(game_state,int(col)-1)
    except e:
        print('Unsucessful')
        raise e
        
    return game_state

def pop_option(game_state:ConnectFourGameState,col:int)-> ConnectFourGameState:
    '''if user chooses p, pop the piece'''

    try:
        
        game_state = connectfour.pop_piece(game_state,int(col)-1)
    except e:
        print('Unsucessful')
        raise e
        
    return game_state

    


def _rotate_board(board:ConnectFourGameState)->str:
    '''take a board and rotate into a 7x6 format'''
    for number in _add_a_line():
        print(number,end=' ')
    print()
    for rows in range(BOARD_ROWS):
        for columns in range(BOARD_COLUMNS):
            if board.board[columns][rows] == ' ':
                point = '.'
            else:
                point = board.board[columns][rows]
            print(point,end=' ')
        print()


def _add_a_line()->None:
    '''return a line of numbers'''
    line=[]
    for i in range(1,BOARD_COLUMNS+1):
        line.append(i)
    return line


def _ask_for_col_drop():
    col = int(input("Enter the column you would like to drop the piece in: "))
    return col

def _ask_for_col_pop():
    col = int(input("Enter the column you would like to pop the piece out: "))
    return col

def _ask_for_option():
    option = input("Would you like to (D)rop or (P)op: ").upper().strip()
    return option
