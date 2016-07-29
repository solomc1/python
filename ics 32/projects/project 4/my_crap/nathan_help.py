def check_pieces(self, column:int, row:int)-> None:
        NORTH = self._board[(row -1) ][(column -1) -1] 
        SOUTH = self._board[(row -1) ][(column -1) +1] 
        EAST = self._board[(row -1) +1 ][(column -1)] 
        WEST = self._board[(row -1) -1 ][(column -1)] 
        NORTHEAST = self._board[(row -1) +1][(column -1)-1] 
        NORTHWEST = self._board[(row -1) -1][(column -1)-1]
        SOUTHEAST = self._board[(row -1) +1][(column -1)+1]
        SOUTHWEST = self._board[(row -1) -1][(column -1)+1]
# for the above code, i wouldn't do that.  It will work for this part, but later you will need to define coldelta * i (i stands for the iteration count)
# that's because you want it to iterate without having a constraint on the last iteration

# you need to work in terms of coldelta and rowdelta


        direction = [NORTH,SOUTH,EAST,WEST,NORTHEAST,NORTHWEST,SOUTHEAST,SOUTHWEST]
        for i in direction:
            if i == NONE:
                print("Go!")
				# then try to see if there's a piece of the opposite player next to the current position
					# if there is, then try to find end piece by moving in that direction
					# while you're moving in that direction, add the coordinates of the other player to a list
						# if it hits another piece that belongs to the player, then flip those pieces
						# otherwise do nothing/return False
				
            elif i == BLACK or i == WHITE:
                print("Cannot place piece because b or w is there")
                raise CannotPlacePiece()

# his code
def _check_piece(self, col: int, row: int) -> bool:
	# since i'm lazy, pretend _four_in_a_row is some other function, let's say it's named _validate_piece()
    return _four_in_a_row(board, col, row, 0, 1) \ # you will only be working with col,row,coldelta,and rowdelta
            or _four_in_a_row(board, col, row, 1, 1) \
            or _four_in_a_row(board, col, row, 1, 0) \
            or _four_in_a_row(board, col, row, 1, -1) \
            or _four_in_a_row(board, col, row, 0, -1) \
            or _four_in_a_row(board, col, row, -1, -1) \
            or _four_in_a_row(board, col, row, -1, 0) \
            or _four_in_a_row(board, col, row, -1, 1)

# translate?
# basically, for each time he runs that function, you set 
# the coordinates to board[col+coldelta][row+rowdelta] to check the imediate piece next to it
# there's a catch though, i'll let you know early on, you need to implement a try somewhere in
# this process since it is problematic for pieces that are next to the boarder of the table
# i gotta sleep, i'll leave you with this haha, 
