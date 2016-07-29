#Solomon Chan 40786337

import othello_logic

def get_row_len()->int:
    row_len = input('Enter row length (Any even int from 4-16: ')
    if row_len == "q":
        exit()
    try:
        if row_len == "":
            return 8
        row_len = int(row_len)       
        if row_len%2 == 0 and row_len in range(4,17):
            return row_len
        else:
            print("Length must be even and in range")
            return get_row_len()
            
    except:
        print("Invalid input, please try again")
        return get_row_len()

def get_col_len()->int:
    col_len = input('Enter col length (Any even int from 4-16: ')
    if col_len == "q":
        exit()
    try:
        if col_len == "":
            return 8
        col_len = int(col_len)
        if col_len in range(4,17):
            if col_len%2 == 0:
                return col_len
            else:
                print("The number of columns must be even, please try again.")
                return get_col_len()
        else:
            print("Length must be even and in range")
            return get_col_len() 
    except:
        print("Invalid input, try again")
        return get_col_len()
    

def get_turn()->bool:
    '''
    Returns true  - white first
            false - black first
    '''
    turn = input('Who goes first? \n (B)lack or (W)hite goes first: ').upper()
    if turn == "Q":
        exit()
    if turn == "W":
        return True
    elif turn == "B" or turn == "":
        return False
    else:
        print("Invalid input, try again")
        return get_turn()

def get_top_left()->bool:
    '''
    Returns true  - for classic, white in the top left, board type
            false - for inverted, black in the top left, board type
    '''
    top_left = input("Top Left Piece: (B)lack or (W)hite: ").upper()
    if top_left == "Q":
        exit()
    if top_left == "W":
        return True
    if top_left == "B" or top_left == "":
        return False
    else:
        print("Invalid input, try again")
        return get_top_left()

def get_match_type():
    '''
    Returns true for most wins, false for least wins
    '''
    match_type = input("(M)ost or (L)east pieces to win the game: ").upper()
    if match_type == "Q":
        exit()
    if match_type == "L":
        return False
    elif match_type == "M" or match_type == "":
        return True
    else:
        print("Invalid input, try again")
        return get_match_type()

def parse_loc_input(loc_str: str)->(int, int):
    info = loc_str.split(sep=",")
    if(len(info) >= 2):
        return int(info[0].strip()), int(info[1].strip())
    else:
        raise ValueError()

def display_board(board : othello_logic.Board)->None:
    print("White total: %d\tBlack total: %d" % (board.num_white_pieces, board.num_black_pieces))
    print()
    print(" -", end="")
    
    for i in range(board.cols):
        print((i + 1), end="")
    print("-")
    
    for y in range(board.rows):
        print("%0d|" % (y + 1), end="")
        for x in range(board.cols):
            board_piece = board.piece_at(othello_logic.Point(x,y))
            if board_piece == othello_logic.Piece.WHITE:
                print("W", end="")
            elif board_piece == othello_logic.Piece.BLACK:
                print("B", end="")
            else:
                print(".", end="")
        
        print("|")
        
    print(" ", end="")


def get_info()->othello_logic.Othello:
    while True:
        row_len = get_row_len()  
        col_len= get_col_len()
        turn = get_turn()
        top_left = get_top_left()
        match_type = get_match_type()
        try:
            return othello_logic.Othello(row_len,col_len,turn,top_left, match_type)
        except othello_logic.InitialConditionsException as e:
            print("%s\nSet up failed, please try again." % e)
            continue

def make_move()->None:
    while True:
        move = input('Where do you want to place your next piece?\n[row, column]: ')
        if move == "q":
            exit()
        try:
            row, col = parse_loc_input(move)
            game.make_move(row, col)
            return
        except ValueError:
            print("Row and column must be numbers separated by a comma, please try again.")
        except othello_logic.InvalidMoveException as e:
            print("%s, please try again." % e)
            continue
        

def user_interface():
    while not game.game_over():
        display_board(game.board)
        if(game.current_player == othello_logic.Piece.WHITE):
            print()
            print("White's turn")
        if(game.current_player == othello_logic.Piece.BLACK):
            print()
            print("Blacks's turn")
        make_move()
        
    display_board(game.board)
    print("Game Over!")
    winner = game.winner()
    
    if winner == othello_logic.Piece.WHITE:
        print("White Wins!")
    elif winner == othello_logic.Piece.BLACK:
        print("Black Wins!")
    elif winner == othello_logic.Piece.TIE:
        print("Its a tie!")
    else:
        print("Unknown error, Noone has won.")      
        
if __name__ == '__main__':
    print('Welcome to Othello! \n * items in settings are the default when nothing is entered. \n Type q anytime to quit.\n')
    game = get_info()
    user_interface()
