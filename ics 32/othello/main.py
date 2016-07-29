'''
Othello CLI

@author: Kyle Brodie
'''
import othello

def get_num_rows()->int:
    row_len_str = input("How many rows should the Othello board have?\n[*8 or any even integer from 4-16]: ")
    if row_len_str == "q":
        exit()
    try:
        if row_len_str == "":
            return 8
        row_len = int(row_len_str)
        if 4 <= row_len <= 16:
            if row_len % 2 == 0:
                return row_len
            else:
                print("The number of rows must be even, please try again.")
                return get_num_rows()
        else:
            print("The number of rows must be in the range 4 to 16 inclusive, please try again.")
            return get_num_rows()
    except:
        print("Numbers only, please try again.")
        return get_num_rows()

def get_num_cols()->int:
    col_len_str = input("How many columns?\n[*8 or any even integer from 4-16]: ")
    if col_len_str == "q":
        exit()
    try:
        if col_len_str == "":
            return 8
        col_len = int(col_len_str)
        if 4 <= col_len <= 16:
            if col_len % 2 == 0:
                return col_len
            else:
                print("The number of columns must be even, please try again.")
                return get_num_cols()
        else:
            print("The number of columns must be in the range 4 to 16 inclusive, please try again.")
            return get_num_cols()
    except:
        print("Numbers only, please try again.")
        return get_num_cols()

def get_first_player()->bool:
    '''
    Returns true  - white first
            false - black first
    '''
    turn = input('Who goes first?\n[*(B)lack or (W)hite]: ').upper()
    if turn == "Q":
        exit()
    if turn == "W":
        return True
    elif turn == "B" or turn == "":
        return False
    else:
        print("Invalid input, please try again.")
        return get_first_player()

def get_board_type()->bool:
    '''
    Returns true  - for classic, white in the top left, board type
            false - for inverted, black in the top left, board type
    '''
    board_type = input("What should the opening board style be?\n[*(C)lassic: White starts in the top left or (I)verted: Black starts in the top left]: ").upper()
    if board_type == "Q":
            exit()
    if board_type == "I":
        return False
    elif board_type == "C" or board_type == "":
        return True
    else:
        print("Invalid input, try again")
        return get_board_type()

def get_win_type()->bool:
    '''
    Returns true for most wins, false for least wins
    '''
    win_type = input("How should the winner be decided? [*(M)ost or (L)east pieces]: ").upper()
    if win_type == "Q":
            exit()
    if win_type == "L":
        return False
    elif win_type == "M" or win_type == "":
        return True
    else:
        print("Invalid input, please try again.")
        return get_win_type()

def parse_loc_input(loc_str: str)->(int, int):
    info = loc_str.split(sep=",")
    if(len(info) >= 2):
        return int(info[0].strip()), int(info[1].strip())
    else:
        raise ValueError()

def print_board(board : othello.Board)->None:
    print("White total: %d\tBlack total: %d" % (board.num_white_pieces, board.num_black_pieces))
    
    print(" -", end="")
    for i in range(board.cols):
        print((i + 1), end="")
    print("-")
    
    for y in range(board.rows):
        print("%0d|" % (y + 1), end="")
        for x in range(board.cols):
            board_piece = board.piece_at(othello.Point(x,y))
            if board_piece == othello.Piece.WHITE:
                print("W", end="")
            elif board_piece == othello.Piece.BLACK:
                print("B", end="")
            else:
                print("-", end="")
        
        print("|")
        
    print(" ", end="")
    for _ in range(board.cols + 2):
        print("-", end="")
    print()

def set_up()->othello.Othello:
    while True:
        rows = get_num_rows()  
        cols= get_num_cols()
        board_type = get_board_type()
        white_first = get_first_player()
        win_type = get_win_type()
        try:
            return othello.Othello(rows, cols, white_first, board_type, win_type)
        except othello.InitialConditionsException as e:
            print("%s\nSet up failed, please try again." % e)
            continue
        
def make_move()->None:
    while True:
        loc_str = input('Where do you want to place your next piece?\n[row, column]: ')
        if loc_str == "q":
            exit()
        try:
            row, col = parse_loc_input(loc_str)
            game.make_move(row, col)
            return
        except ValueError:
            print("Row and column must be numbers separated by a comma, please try again.")
        except othello.InvalidMoveException as e:
            print("%s, please try again." % e)
            continue
        
if __name__ == '__main__':
    print("Welcome to CLI Othello!\nAsterisked items in the settings are the default when nothing is entered.\nType q anytime to quit.\n")
    game = set_up()
    
    while not game.game_over():
        print_board(game.board)
        if(game.current_player == othello.Piece.WHITE):
            print("White's turn")
        if(game.current_player == othello.Piece.BLACK):
            print("Blacks's turn")
        make_move()
        
    print_board(game.board)
    print("Game Over!")
    winner = game.winner()
    
    if winner == othello.Piece.WHITE:
        print("White Wins!")
    elif winner == othello.Piece.BLACK:
        print("Black Wins!")
    elif winner == othello.Piece.TIE:
        print("Its a tie!")
    else:
        print("HACKER ALERT! The winner is None!")