def place_4_pieces

def valid_move

def place_piece

def full_board

def win

def new_board

turn

row

column

board

top_left

most = false/true

WHITE = 'W'
BLACK = 'B'
class OthelloGS:
    def __init__(self, column: int, row:int, top_left:str, most:bool):
        self._turn = turn
        self._row = row
        self._most = most
        self._column = column
        self._top_left = top_left
        self._board = self._new_board()

    def place_4_pieces(self)->None:
        if self._top_left == WHITE:
            self._board[(column/2) -1][(row/2)-1] = WHITE
            self._board
            self._board
            self._board
        elif self._top_left == BLACK:
            
    
    def place_piece(self, column:int, row:int)->None
        pass
    
    def full_board(self)->bool:
        for i in lst:
            if i ! = '':
                return false
        return True
            

    def win(self)->str:
        pass

    def new_board(self):
        self.place_4_pieces()


    
        
