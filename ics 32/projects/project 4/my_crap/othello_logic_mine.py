#most = false/true
#Solomon Chan 40786337

WHITE = 'W'
BLACK = 'B'
NONE = ' '

class game_state:
    def __init__(self, column: int, row:int, turn:str, top_left:str): # most:bool
        self._turn = turn
        self._row = row
  #      self._most = most
        self._column = column
        self._top_left = top_left
        self._board = self.new_board()
        self.place_4_pieces()

        

    def new_board(self):
        board = []
        for rows in range(self._row):
            rows = []
            for col in range(self._column):
                rows.append('.')
            board.append(rows)
        return board
    

    def place_4_pieces(self)->None:
        if self._top_left == WHITE:
            self._board[int(self._column/2) -1][int(self._row/2)-1] = WHITE
            self._board[int(self._column/2) -1][int(self._row/2)] = BLACK
            self._board[int(self._column/2) ][int(self._row/2)] = WHITE
            self._board[int(self._column/2) ][int(self._row/2)-1] = BLACK
        elif self._top_left == BLACK:
            self._board[int(self._column/2) -1][int(self._row/2)-1] = BLACK
            self._board[int(self._column/2) -1][int(self._row/2)] = WHITE
            self._board[int(self._column/2) ][int(self._row/2)] = BLACK
            self._board[int(self._column/2) ][int(self._row/2)-1] = WHITE
    
    def place_piece(self, column:int, row:int)->None:
        if self._turn == BLACK:
            self._board[row -1 ][column -1] = BLACK
            self.swap_turn()
        else:   
            self._board[row -1 ][column -1] = WHITE
            self.swap_turn()

    def _board_col_index(self, sub_column: int) -> bool:
        return -1 < sub_column < self._column

    def _board_row_index(self, sub_row: int) -> bool:
        return -1 < sub_row < self._row

    def _check_board(self, column: int, row:int)->list:
        if self._turn == WHITE:
            opp_turn = BLACK
        else:
            opp_turn = WHITE
        result = []
        deltas = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

        for i in deltas:
            if self._board[(row - 1)+ i[0]][(column - 1)+i[1]] == '.':
                for cols in range(column-1, self._column):
                    for subrow in range(row-1, self._row):
                        sub = []
                        row_change = (row - 1) + subrow
                        col_change = cols - (column -1)
                        row_now = subrow
                        column_now = cols

                        while self._board_index(column_now, row_now):
                            if self._board[column_now][row_now] == self._turn:
                                result.extend(sub)
                                break
                            elif self._board[column_now][row_now] == opp_turn:
                                sub.append((column_now,row_now))
                            else:
                                break
            

                            row_now += row_change
                            column_now += col_change
        
        return result

    


            

    
    

class InvalidMove(Exception):
    pass

                    

##    def _flip_tiles(self, check_board)->None:
##        for i in check_board:
##            if self._board



    def swap_turn(self)->None:
        if self._turn == BLACK:
            self._turn = WHITE
        else:
            self._turn = BLACK

    def num_line(self)->None:
        line=[]
        for i in range(1,self._column+1):
            line.append(i)
        return line

    
class CannotPlacePiece(Exception):
    '''raises an exception when the user tries to place a piece that is
    already there'''
    pass


##def check_pieces(self, column:int, row:int)-> None:
##        self._board[(row -1) ][(column -1) -1] = NORTH
##        self._board[(row -1) ][(column -1) +1] = SOUTH
##        self._board[(row -1) +1 ][(column -1)] = EAST
##        self._board[(row -1) -1 ][(column -1)] = WEST
##        self._board[(row -1) +1][(column -1)-1] = NORTHEAST
##        self._board[(row -1) -1][(column -1)-1] = NORTHWEST
##        self._board[(row -1) +1][(column -1)+1] = SOUTHEAST
##        self._board[(row -1) -1][(column -1)+1] = SOUTHWEST
##
##        direction = [NORTH,SOUTH,EAST,WEST,NORTHEAST,NORTHWEST,SOUTHEAST,SOUTHWEST]
##        for i in direction:
##            if i == NONE:
##                print("Go!")
##            elif i == BLACK or i == WHITE:
##                print("Cannot place piece because b or w is there")
##                raise CannotPlacePiece()

##    def _check_move(board: [[str]], col: int, row: int, coldelta: int, rowdelta: int) -> bool:
##        deltas = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
##        start_tiles = self._board[col][row]
##        result = []
##        if self._turn == WHITE:
##            opp_turn = BLACK
##        else:
##            opp_turn = WHITE
##
##        if start_tiles == '.':
##            raise InvalidMove()
##            return False
##        else:
##            for i in deltas:
##                try:
##                    if self._board[(col-1)+i[0]][(row-1)+i[1]] == opp_turn:
##                        _board_index
##                    else:
##                        return False
##                except:
##                    pass
##
##    

        
