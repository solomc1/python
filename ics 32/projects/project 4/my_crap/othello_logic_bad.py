#Solomon Chan 40786337

BLACK = 'B'
WHITE = 'W'
NONE = ' '

class game_state:

    def __init__(self,row_length:int, col_length:int, turn:str):
        self.turn = turn
        self.row = row_length
        self.col = col_length
        self.board = self.create_board()
        self.add_a_line = self.num_line()
 #       self.initial_board_placement = self.initial_board_placement()
 #       self.copy_board = self.copy_board()
 #       self.place_tile = self.place_tile()
 #       self.swap_turn = self.swap_turn()
 #       self.insert_piece = self.insert_piece()

    def create_board(self,turn:str):
        board = []
        self.num_line()
        for columns in range(self.col):
            rows = []
            for row in range(self.row):
                rows.append('.')
            board.append(rows)
        if self.turn == BLACK:
            return BLACK
        elif self.turn == WHITE:
            return WHITE
        return board

##    def first_move(self):
##        if self.turn == BLACK:
##            return BLACK
##        elif self.turn == WHITE:
##            return WHITE
    
    def num_line(self)->None:
        line=[]
        for i in range(1,self.col+1):
            line.append(i)
        return line

    
            
    #,board: [[str]]) -> [[str]]
##    def copy_board(self):
##        '''Copies the given game board'''
##        copy_board = []
##        for columns in range(self.col):
##            rows = []
##            for row in range(self.row):
##                rows.append('.')
##            copy_board.append(rows)
##        self.display_board(copy_board)
##        return copy_board
    
##    def place_tile(self, y: int, x:int):
##        
##        new_board = copy_board(self.board)
##        new_board[y][x] = self.turn 
        
    def initial_board_placement(self)->None:
        x = int(self.row/2)
        y = int(self.col/2)
        new_board = self.copy_board()
        if self.board[x][y] or self.board[x+1][y+1]:
            self.turn = BLACK
        elif self.board[x+1][y] or self.board[x][y+1]:
            self.turn = WHITE
        
             
            
##    def swap_turn(self):
##        if self.turn == BLACK:
##            self.turn = WHITE
##        else:
##            self.turn = BLACK
##
    
##    
##    def top_left():
##        pass
        
class InvalidOthelloError(Exception):
    '''Raised whenever an invalid move is made'''
    pass


    




        
#def insert_piece()    


    
        

#num = 'B'
#print(first_move(num))
#a = game_state(4,4,'B')
#print(a.initial_board_placement())
#print(a.turn)
#a.swap_turn()
#print(a.turn)



    

def game_over():
    pass
    #return self.board
