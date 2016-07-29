import connectfour

game_state = connectfour.new_game_state()

def board_print(game: connectfour.ConnectFourGameState)-> None:
    for row in range(connectfour.BOARD_ROWS):
        for col in range(connectfour.BOARD_COLUMNS):
            if game.board[col][row]:
                print('.', end = ' ')
            else:
                print(game.board[col][row], end = ' ')
            print()
game_state = connectfour.drop_piece(game_state, 5-1)
board_print(game_state)
                
#1 Create a new game state
#2 ask user to make a move
#3 after each move, check if gamehas ended
# if the game has ended, break the loop
# if not repeat steps 2-3

HOST = 'evil-monkey.ics.uci.edu'
PORT = 4444

import socket
s = socket.socket()
s.connect((HOST,PORT))
socket_in = s.makefile('r')
socket_out = s.makefile('w')

msg = 'I32CFSP_HELLO boo'

socket_out.write(msg + '\r\n')
socket_out.flush()
print(socket_in.readline())

#Sends move to the server,
#Print out the server's move



                
                



































