class cfgamestate:
    def __init__self, columns:int, rows:int, top_left:):
        self._columns = columns
        self._rows = rows
        self._board = self._new_board()
        self._turn = 'R'


    def _new_board(self)->list:
        '''Returns a newly created board'''
        result = []
        for c in range(self._columns):
            temp = []
            for r in range(self._rows):
                temp.append('')
            result.append(temp)
        return result

    def drop_piece(self, column:int)-> None:
        '''Modifies the game board to reflect the dropped piece'''
        self._board[column][row] = self._turn

    def pop_piece(self, column: int) -> None:
        '''Modifies the game board to reflect the popped piece'''
        pass

    def win(self)-> str:
        '''Returns a winner or None'''

'''if someone makes a move, what would be flipped'''
'''what tiles would be flipped'''
'''call it 8 times write
