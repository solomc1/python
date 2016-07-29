    def _check_board(self, column: int, row:int)->list:
        if self._turn == WHITE:
            opp_turn = BLACK
        else:
            opp_turn = WHITE
        result = []
        deltas = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

        for i in deltas:

            if self._board[(row - 1)+ i[0]][(column - 1)+i[1]] == '.':
                for cols in range(column, self._column):
                    for subrow in range(row, self._row):
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
                            
            
##    for _ in range(board.cols + 2):
##        print("-", end="")
    print()
    
##    self.num_line
##    for i in self.num_line():
##        print(i,end=' ')
##    print()
##    for rows in range(self._row):
##        for columns in range(self._column):
##            if self._board[columns][rows] == ' ':
##                dot = '.'
##            else:
##                dot = self._board[columns][rows]
##            print(dot,end=' ')
##        print()

    
        
##        if self._turn == BLACK:
##            if self._board[(row -1) ][(column -1)] == NONE \
##               or self._board[(row -1) ][(column -1)] == WHITE \
##               or self._board[(row -1) ][(column -1)] == NONE:
                


        
##        '''if someone makes a move, what would be flipped'''
##        '''what tiles would be flipped'''
##        '''call it 8 times write'''
        
    
    def _full_board(self)->bool:
        for i in lst:
            if i != '':
                return False
        return True
            

##    def win(self)->str:
##        WINNER = NONE
##    
##        for col in range(self._column):
##            for row in range(self._row):
##                if _winning_sequence_begins_at(game_state.board, self._column, self._row):
##                    if WINNER == NONE:
##                        WINNER = game_state.board[self._column][row]
##                    elif winner != game_state.board[self._column][row]:
##                        return self.swap_turn()
##
##        return WINNER

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

