#self._board = board
#self._columns = columns
#self._rows = rows
#self._turn = turn

def _index_in_board(self, column: int, row: int) -> bool:
    return -1 < column < self._columns and -1 < row < self._rows

def _valid_move:
    if len(list) > 0:
        return list

def _flip_pieces(self, pieces_to_flip) -> None:
    for position in pieces_to_flip:
        self_board[position[0]

def _pieces_to_flip(self, column: int, row: int)->list:
    if self._turn == 'B':
        opponent ='W'
    else:
        opponent = 'B'

    result = []

    if self._board[column-1][row - 1] == None:
        for col in range(column - 2, column +1):
            for r in range(row - 2, row +1):
                temp = []
                col_change = col - (column -1)
                row_change = r - (row - 1)
                curr_col = col
                curr_row = r

                while self._index_in_board(curr_col, curr_row):
                    if self._board[curr_col][curr_row] == opponent:
                        temp.append((curr_col, curr_row))
                    elif self._board[curr_col][curr_row] == self._turn:
                        result.extend(temp)
                        break
                    else:
                        break

                    curr_col += col_change
                    curr_row += row_change

    return result
