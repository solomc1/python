'''
Created on 2 Mar 2014

@author: kylebrodie
'''
import othello
import unittest

class TestOthello(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test4x4WhiteWins(self):
        game = othello.Othello(4, 4, False, True, True)
        game.make_move(2, 1)
        game.make_move(1,1)
        game.make_move(4,3)
        game.make_move(2,4)
        game.make_move(1,3)
        game.make_move(4,2)
        game.make_move(4,1)
        game.make_move(3,1)
        game.make_move(1,2)
        game.make_move(1,4)
        game.make_move(3,4)
        game.make_move(4, 4)
        assert game.game_over()
        assert game.winner() == othello.Piece.WHITE


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TestOthello.test4x4WhiteWins']
    unittest.main()