# Tiancheng Xu 74436321 and Solomon Chan 40786337. ICS 32 Lab 7. connectfour_console.

import collections
import connectfour
import linkui

ConnectFourGameState = collections.namedtuple('ConnectFourGameState', ['board', 'turn'])

BOARD_COLUMNS = 7
BOARD_ROWS = 6

NONE = ' '
RED = 'R'
YELLOW = 'Y'

class InvalidConnectFourMoveError(Exception):
    '''Raised whenever an invalid move is made'''
    pass


class ConnectFourGameOverError(Exception):
    '''
    Raised whenever an attempt is made to make a move after the game is
    already over
    '''
    pass

def rematch()->None:
    '''asks the player if the player wants a rematch'''
    while True:
        opt = input('One more game(Y)es or (N)o? ').upper().strip()
        if opt == 'Y':
            user_interface()
        elif opt == 'N':
            print("Goodbye!")
            break
        else:
            print("Invalid")

def user_interface()->None:
    print("Welcome to Connect Four!")
    last_state = connectfour.new_game_state()
    linkui._rotate_board(last_state)
    while True:
        option = linkui.ask_for_option()
        if option == 'D':
            try:
                
                col = linkui.ask_for_col_drop()
            except:
                print('Invalid value.')
            else:
                last_state = linkui.option_d(last_state,col)
        elif option == 'P':
            try:
                
                col = linkui.ask_for_col_pop()
            except:
                print('Invalid value.')
            else:
                last_state = linkui.option_p(last_state,col)
        else:
            print('Invalid Command.')
            
        

        if connectfour.winning_player(last_state) != ' ':
            print("Player " + connectfour.winning_player(last_state) + " wins!")
            break
    rematch()


            





if __name__ == '__main__':
    user_interface()
    
