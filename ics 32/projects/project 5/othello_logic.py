#Solomon Chan 40786337
from enum import Enum
from copy import copy

class InitialConditionsException(Exception):
    pass
        
class InvalidMoveException(Exception):
    pass

class Point:
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)
        
    def __eq__(self, other):
        if(isinstance(other.x, int) and isinstance(other.y, int)):
            return self.x == other.x and self.y == other.y
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
        
    def __iadd__(self, other):
        if(isinstance(other.x, int) and isinstance(other.y, int)):
            self.x += other.x
            self.y += other.y
            return self
        return NotImplemented

    def __isub__(self, other):
        if(isinstance(other.x, int) and isinstance(other.y, int)):
            self.x -= other.x
            self.y -= other.y
            return self
        return NotImplemented
    
    def __add__(self, other):
        if(isinstance(other.x, int) and isinstance(other.y, int)):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if(isinstance(other.x, int) and isinstance(other.y, int)):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __radd__(self, other):
        if(isinstance(other.x, int) and isinstance(other.y, int)):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __rsub__(self, other):
        if(isinstance(other.x, int) and isinstance(other.y, int)):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented
    
class Piece(Enum):
    BLACK = False
    WHITE = True
    NONE = None
    TIE = [WHITE, BLACK]
    
    def __invert__(self):
        if self == Piece.WHITE:
            return Piece.BLACK
        elif self == Piece.BLACK:
            return Piece.WHITE
        elif self == Piece.NONE:
            return Piece.NONE
        else:
            return Piece.TIE
        
    @staticmethod
    def is_playable_piece(piece)->bool:
        '''
        Returns whether or not this piece is playable or not
        '''
        return piece == Piece.WHITE or piece == Piece.BLACK    
    
        
    

class Direction(Enum):
    North = (0, -1)
    South = (0, 1)
    East = (1, 0)
    West = (-1, 0)
    NorthEast = (1, -1)
    SouthEast = (1, 1)
    NorthWest = (-1, -1)
    SouthWest = (-1, 1)
        
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y



class Othello:
    '''
    Runs and contains the state of an Othello game. One game per instance.
    UI's should check the current player before making a move, because in
    certain edge cases the same player may move twice.
    '''

    def __init__(self, rows: int, cols: int, white_starts: bool, orignal_board: bool, most_wins: bool):
        '''
        Sets up the game with the provided initial conditions:
            rows -            number of rows on the board
            cols -            number of columns on the board
            white_starts -    true: white moves first
                              false: black moves first
            orignal_board -   true: white starts in the top left
                              false: black starts in the top left
            most_wins -       true: the player with the most pieces wins
                              false: the player with the least pieces wins
        '''
        self.board = Board(rows, cols, orignal_board)
        self.most_wins = most_wins
        self.current_player = Piece.WHITE if white_starts else Piece.BLACK
        
    def make_move(self, row: int, col: int)->None:
        '''
        Attempts to place the current player's piece at the specified row and column on the board.
        Throws an exception if there was an error making the move. E.g. row and column outside of
        the board, illegal move, game over, etc.
        '''
        if self.game_over():
            raise InitialConditionsException("Game Over")
        
        p = Point(col - 1, row - 1)
        self.board.make_move(p, self.current_player)
        self.current_player = ~self.current_player
        
        if not self.board.has_valid_moves(self.current_player):
            self.current_player = ~self.current_player
            
    def game_over(self)->bool:
        return (not self.board.has_valid_moves(Piece.WHITE)) and (not self.board.has_valid_moves(Piece.BLACK))
    
    def winner(self)->Piece:
        if self.board.num_white_pieces == self.board.num_black_pieces:
            return Piece.TIE
        elif self.board.num_white_pieces > self.board.num_black_pieces:
            return Piece.WHITE if self.most_wins else Piece.BLACK
        else:
            return Piece.BLACK if self.most_wins else Piece.WHITE

class Board:
    '''
    Represents an Othello Board
    '''
    def __init__(self, rows: int, cols: int, original_board: bool):
        if (4 <= rows <= 16) and (rows % 2 == 0):
            self.rows = rows
        else:
            raise InitialConditionsException("Rows must be an even number between 4 and 16, inclusive.")
        
        if (4 <= cols <= 16) and (cols % 2 == 0):
            self.cols = cols
        else:
            raise InitialConditionsException("Columns must be an even number between 4 and 16, inclusive.")
        
        self.original_board = original_board
        self.num_white_pieces = 0
        self.num_black_pieces = 0
        self._init_board()
        
    def _init_board(self)->None:
        self._board = []
        self._empty_spaces = []
        for y in range(self.cols):
            row = []
            for x in range(self.rows):
                row.append(Piece.NONE)
                self._empty_spaces.append(Point(x,y))
            self._board.append(row)
        
        p = Point(self.cols / 2 - 1, self.rows / 2 - 1)
        white = Piece.WHITE if self.original_board else Piece.BLACK
        black = ~white
        self.set_piece(p, white)
        self.set_piece(p + Direction.East, black)
        self.set_piece(p + Direction.SouthEast, white)
        self.set_piece(p + Direction.South, black)

    def on_board(self, p: Point)->bool:
        return (-1 < p.x < self.cols) and (-1 < p.y < self.rows)
    
    def _inc_piece_total(self, piece: Piece)->None:
        if piece == Piece.WHITE:
            self.num_white_pieces += 1
        elif piece == Piece.BLACK:
            self.num_black_pieces += 1
            
    def _dec_piece_total(self, piece: Piece)->None:
        if piece == Piece.WHITE:
            self.num_white_pieces -= 1
        elif piece == Piece.BLACK:
            self.num_black_pieces -= 1
    
    def set_piece(self, p: Point, piece: Piece)->None:
        board_piece = self.piece_at(p)
        if board_piece == Piece.NONE:
            self._empty_spaces.remove(p)
            self._board[p.y][p.x] = piece
            self._inc_piece_total(piece)
        elif board_piece != piece:
            self._dec_piece_total(board_piece)
            self._board[p.y][p.x] = piece
            self._inc_piece_total(piece)  

    def piece_at(self, p: Point)->Piece:
        if self.on_board(p):
            return self._board[p.y][p.x]
        return None

    def occupied(self, p: Point)->bool:
        return Piece.is_playable_piece(self.piece_at(p))

    def neighbor_pieces(self, p: Point)->[Piece]:
        neighbors = []
        for d in Direction:
            neighbors.append(self.neighbor_piece(p, d))
    
    def neighbor_piece(self, p: Point, d: Direction)->Piece:
        return self.piece_at(p + d)
    
    def has_valid_moves(self, piece: Piece)->bool:
        if (not Piece.is_playable_piece(piece)) or (len(self._empty_spaces) == 0):
            return False
        for p in self._empty_spaces:
            if self.valid_move(p, piece):
                return True
        return False
    
    def valid_move(self, p: Point, piece: Piece)->bool:
        if (not self.on_board(p)) or self.occupied(p) or (not Piece.is_playable_piece(piece)):
            return False
        
        self._locs_to_flip = []
        paths = 0
        opp_piece = ~piece
        
        for d in Direction:
            if self.neighbor_piece(p, d) == opp_piece:
                if self._valid_path(p, d, piece):
                    paths += 1
        return paths > 0

    def _valid_path(self, p: Point, d: Direction, piece: Piece)->bool:
        opp_piece = ~piece
        to_flip = []
        new_p = copy(p)
        new_p += d
        while(self.on_board(new_p)):
            board_piece = self.piece_at(new_p)
            
            if board_piece == Piece.NONE:
                return False
            elif board_piece == opp_piece:
                to_flip.append(copy(new_p))
            else:
                self._locs_to_flip.extend(to_flip)
                return True
            new_p += d
        return False
    
    def _flip(self, p: Point)->None:
        if(self.on_board(p)):
            piece = self.piece_at(p)
            self.set_piece(p, ~piece)
                
    def _flip_list(self, ps: [Point])->None:
        for p in ps:
            self._flip(p)
                
    def make_move(self, p: Point, piece: Piece)->None:
        if not self.on_board(p):
            raise InvalidMoveException("That location is not on the board")
        if not Piece.is_playable_piece(piece):
            raise InvalidMoveException("Cannot place a NONE piece (How did you do that? Damn hackers :/ )")
        
        if self.valid_move(p, piece):
            self.set_piece(p, piece)
            self._flip_list(self._locs_to_flip)
        else:
            raise InvalidMoveException("That is not a valid move")
