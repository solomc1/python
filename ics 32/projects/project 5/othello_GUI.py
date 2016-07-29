#Solomon Chan 40786337
import tkinter as tk
from tkinter import ttk, constants as const

from othello_logic import InvalidMoveException, Othello, Piece, Point, Board

class OthelloGUI:

    def click_empty(self, event) -> None:
        x = self._canvas.canvasx(event.x)
        y = self._canvas.canvasy(event.y)
        item = self._canvas.find_closest(x, y)[0]
        tags = self._canvas.gettags(item)
        row = int(tags[1]) + 1
        col = int(tags[0]) + 1
        
        try:
            self.game.make_move(row, col)
        except InvalidMoveException as e:
            tk.messagebox.showerror(title="Error", icon="warning", message=str(e))
            return
        self.refresh_board(None)
            
                

    def refresh_board(self,event) -> None:
        WHITE = self.game.board.num_white_pieces
        BLACK = self.game.board.num_black_pieces
        if not self.game.game_over():
            self.refresh_labels()
            self.draw_board()
        else:
            if WHITE > BLACK:
                tk.messagebox.showinfo(title="Game Over", icon="warning", message="White Wins!   White total: %d   Black total: %d" % (self.game.board.num_white_pieces,
                                                                                                         self.game.board.num_black_pieces))
                exit()
                    
            elif WHITE < BLACK:
                tk.messagebox.showinfo(title="Game Over", icon="warning", message=("Black Wins!   White total: %d   Black total: %d" % (self.game.board.num_white_pieces,self.game.board.num_black_pieces)))
                exit()
            elif WHITE == BLACK:
                tk.messagebox.showinfo(title="Game Over", icon="warning", message="Draw.   White total: %d   Black total: %d" % (self.game.board.num_white_pieces,self.game.board.num_black_pieces))
                exit()
            else:
                tk.messagebox.showinfo(title="Game Over", icon="warning", message="Unknown error, Noone has won.")
                exit()
        
            
            
    
    def draw_board(self) -> None:
        
        self._canvas.delete(tk.constants.ALL)
        
        col_ratio = self._canvas.winfo_width() / self.columns
        row_ratio = self._canvas.winfo_height() / self.rows
        
        for col in range(self.columns):
            for row in range(self.rows):
                p = Point(col, row)  # board point
                p1 = Point(col * col_ratio, row * row_ratio)  # canvas point one
                p2 = Point((col + 1) * col_ratio, (row + 1) * row_ratio)  # canvas point two
                
                board_piece = self.game.board.piece_at(p)
                
                if(Piece.is_playable_piece(board_piece)):
                    self.draw_piece(board_piece, p1, p1, p2)
                else:
                    rect = self.draw_empty(p, p1, p2)
                    self._canvas.tag_bind(rect, '<ButtonPress-1>', self.click_empty)

    def draw_empty(self, p: Point, p1: Point, p2: Point):
        return self._canvas.create_rectangle(p1.x, p1.y, p2.x, p2.y, fill='white', outline='black', tag=(p.x, p.y))

    def draw_piece(self, piece: Piece, p: Point, p1: Point, p2: Point) -> None:
        if(piece == Piece.WHITE):
            self._canvas.create_rectangle(p1.x, p1.y, p2.x, p2.y, fill='white', outline='black', tag=(p.x, p.y))
            self._canvas.create_oval(p1.x, p1.y, p2.x, p2.y, fill='white', outline='blue', tag=(p.x, p.y))
        elif(piece == Piece.BLACK):
            self._canvas.create_rectangle(p1.x, p1.y, p2.x, p2.y, fill='white', outline='black', tag=(p.x, p.y))
            self._canvas.create_oval(p1.x, p1.y, p2.x, p2.y, fill='black', outline='blue', tag=(p.x, p.y))
    
    def _configure_game(self) -> None:
        config = ConfigureGUI()
        config.start()
        self.game = config.getOthello()

    def refresh_labels(self)-> None:
        self.current_player_str = "White" if self.game.current_player == Piece.WHITE else "Black"
        
        
        self._label["text"] = "White total: %d\tTurn: %s\tBlack total: %d" % (self.game.board.num_white_pieces,
                                                                                                 self.current_player_str,
                                                                                                 self.game.board.num_black_pieces)
        


        
##    def check_game_over(self)-> None:
##        while not game.game_over():
            
            
    

    def _init_game(self, board: Board) -> None:
        self._root = tk.Tk()
        self._root.title("Othello")
        self.rows = self.game.board.rows
        self.columns = self.game.board.cols
        self._canvas = tk.Canvas(master=self._root, height=50 * self.rows, width=50 * self.columns, background='white')
        self._canvas.bind("<Configure>", self.refresh_board)
        self.current_player_str = "White" if self.game.current_player == Piece.WHITE else "Black"
         
        self._label = tk.Label(self._root, text= "White total: %d\tTurn: %s\tBlack total: %d" % (self.game.board.num_white_pieces,
                                                                                                 self.current_player_str,
                                                                                                 self.game.board.num_black_pieces),
                                                                                      fg='black',
                                                                                      font="Helvetica 16 bold")      
        
        self._label.pack(side=tk.constants.TOP)
        self._canvas.pack(fill=tk.constants.BOTH, expand=tk.constants.YES)

    

    def start(self) -> None:
        self._configure_game()
        self._init_game(Board)
        
        self._root.mainloop()
        

class ConfigureGUI:

    def __init__(self):
        #
        # Main application window
        #
        self._root = tk.Tk()
        self._root.title("Othello")
        self._root.focus()
        self._root.minsize(400, 250)
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(1, weight=1)
        
        #
        # Welcome labels frame
        #
        welcome_frame = ttk.Frame(self._root, borderwidth=5)
        welcome_label = ttk.Label(welcome_frame, text="Welcome to GUI Othello!")
        
        welcome_frame.grid(row=0, column=0, sticky=(const.N, const.S, const.E, const.W))
        welcome_label.grid(row=0, column=0, padx=5, pady=5)
        
        welcome_frame.columnconfigure(0, weight=1)
        
        #
        # Main frame (configuration
        #
        self._content = ttk.Frame(self._root)
        
        self._row = tk.IntVar()
        row_label = ttk.Label(self._content, text="Number of Rows: ")
        row_picker = ttk.Combobox(self._content, state="readonly", textvariable=self._row, values=[4, 6, 8, 10, 12, 14, 16])
        row_picker.set(8)
        
        self._col = tk.IntVar()
        col_label = ttk.Label(self._content, text="Number of Columns: ")
        col_picker = ttk.Combobox(self._content, state="readonly", textvariable=self._col, values=[4, 6, 8, 10, 12, 14, 16])
        col_picker.set(8)
        
        self._white_starts = tk.BooleanVar()
        white_starts_label = ttk.Label(self._content, text="White starts: ")
        white_starts_picker = ttk.Combobox(self._content, state="readonly", textvariable=self._white_starts, values=[True, False])
        white_starts_picker.current(1)
        
        self._classic_board_str = tk.StringVar()
        classic_board_str_label = ttk.Label(self._content, text="Opening Board Style: ")
        classic_board_str_picker = ttk.Combobox(self._content, state="readonly", textvariable=self._classic_board_str)
        classic_board_str_picker["values"] = ["Classic (white starts in the top left)", "Inverted (black starts in the top left)"]
        classic_board_str_picker.set("Classic (white starts in the top left)")
        
        self._most_wins = tk.BooleanVar()
        most_wins_label = ttk.Label(self._content, text="Most Pieces Wins: ")
        most_wins_picker = ttk.Combobox(self._content, state="readonly", textvariable=self._most_wins, values=[True, False])
        most_wins_picker.current(0)

        self._content.grid(row=1, column=0, sticky=(const.N, const.S, const.E, const.W))
        
        row_label.grid(row=0, column=0, sticky=(const.N, const.E), padx=5, pady=2)
        row_picker.grid(row=0, column=1, columnspan=2, sticky=(const.N, const.W, const.E), padx=2, pady=2)
        col_label.grid(row=1, column=0, sticky=(const.N, const.E), padx=5, pady=2)
        col_picker.grid(row=1, column=1, columnspan=2, sticky=(const.N, const.W, const.E), padx=2, pady=2)
        white_starts_label.grid(row=2, column=0, sticky=(const.N, const.E), padx=5, pady=2)
        white_starts_picker.grid(row=2, column=1, columnspan=2, sticky=(const.N, const.W, const.E), padx=2, pady=2)
        classic_board_str_label.grid(row=3, column=0, sticky=(const.N, const.E), padx=5, pady=2)
        classic_board_str_picker.grid(row=3, column=1, columnspan=2, sticky=(const.N, const.W, const.E), padx=2, pady=2)
        most_wins_label.grid(row=4, column=0, sticky=(const.N, const.E), padx=5, pady=2)
        most_wins_picker.grid(row=4, column=1, columnspan=2, sticky=(const.N, const.W, const.E), padx=2, pady=2)
        
        self._content.columnconfigure(0, minsize=70)
        self._content.columnconfigure(1, weight=1, minsize=50)
        self._content.columnconfigure(2, weight=1, minsize=50)
        self._content.rowconfigure(0, weight=1, minsize=30)
        self._content.rowconfigure(1, weight=1, minsize=30)
        self._content.rowconfigure(2, weight=1, minsize=30)
        self._content.rowconfigure(3, weight=1, minsize=30)
        self._content.rowconfigure(4, weight=1, minsize=30)
        
        #
        # Play/Quit buttons frame
        #
        play_frame = ttk.Frame(self._root, borderwidth=5)
        play = ttk.Button(play_frame, text="Play", command=self._root.destroy)
        cancel = ttk.Button(play_frame, text="Quit", command=exit)
        
        play_frame.grid(row=2, column=0, sticky=(const.N, const.S, const.E, const.W))
        play.grid(row=0, column=0, sticky=(const.N, const.S, const.E), padx=5, pady=2)
        cancel.grid(row=0, column=1, sticky=(const.N, const.S, const.W), padx=5, pady=2)
        
        play_frame.columnconfigure(0, weight=1)
        play_frame.columnconfigure(1, weight=1)

    def start(self) -> None:
        self._root.mainloop()

    def getOthello(self) -> Othello:
        return Othello(self._row.get(), self._col.get(), self._white_starts.get(), True if (self._classic_board_str.get() == "Classic (white starts in the top left)") else False, self._most_wins.get())       

if __name__ == '__main__':
    app = OthelloGUI()
    app.start()
