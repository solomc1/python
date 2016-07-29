from tkinter import Tk, Frame, Canvas, IntVar, StringVar, BooleanVar, ttk, messagebox, constants as const
from random import randint
from othello_logic import InvalidMoveException, Othello, Piece, Point

class OthelloGUI:

    n = 1

    def __init__(self):
        self._configure_game()
        self._init_game()
        self.refresh_board()

    def _configure_game(self) -> None:
        config = ConfigureGUI()
        config.start()
        self.game = config.getOthello()

    def _init_game(self) -> None:
        # Make some game constants more easily accessible
        self.rows = self.game.board.rows
        self.columns = self.game.board.cols
        
        #
        # Main window
        #
        self._root = Tk()
        self._root.title("Othello")
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(2, weight=1)
        self._root.minsize(50 * self.columns + 100, 50 * self.rows + 100)
        
        #
        # Score Label
        #
        score_frame = Frame(self._root)
        self._score_label = ttk.Label(score_frame, background="white", foreground="black", text="TEMPORARY LABEL") #TODO: compute label text
        
        score_frame.grid(row=0, column=0, sticky="ew")
        self._score_label.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        
        score_frame.columnconfigure(0, weight=1)
        
        #
        # Info Label
        #
        info_frame = Frame(self._root)
        self._info_label = ttk.Label(info_frame, text="", background="white", foreground="black")
        
        info_frame.grid(row=1, column=0, sticky="ew")
        self._info_label.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        
        info_frame.columnconfigure(0, weight=1)
        
        #
        # Game content (Othello board)
        #
        self._content = Frame(self._root)
        self._content.grid(row=2, column=0, sticky="nsew")
        
        self.cells = []
        
        for row in range(self.rows):
            for col in range(self.columns):
                self.cells.append(self._build_cell(row, col))
                self._content.columnconfigure(col, weight=1)

            self._content.rowconfigure(row, weight=1)

    def _build_cell(self, row: int, col: int) -> Frame:
        cell = Frame(self._content, borderwidth=5, relief=const.SUNKEN, height=50, width=50)
        
        cell._canvas = Canvas(master=cell, height=50, width=50)
        cell.row = row
        cell.col = col
        cell.bound = False
        
        cell.grid(row=row, column=col, sticky="nsew")
        cell.columnconfigure(0, weight=1)
        cell.rowconfigure(0, weight=1)
        
        cell._canvas.grid(row=0, column=0, sticky="nsew")
        return cell

    def refresh_board(self) -> None:
        self.draw_board()
        self._score_label["text"] = "I update when things happen. n = %d" % self.n
        self.n = self.n + 1
    
    def draw_board(self) -> None:
        for cell in self.cells:
            p = Point(cell.col, cell.row)
            board_piece = self.game.board.piece_at(p)
            if(Piece.is_playable_piece(board_piece)):
                self.draw_piece(cell, board_piece)
                if cell.bound:
                    cell._canvas.unbind("<ButtonPress-1>", None)
            else:
                cell._canvas.bind("<ButtonPress-1>", self.click_empty)
                cell.bound = True

    def draw_piece(self, cell: Frame, piece: Piece) -> None:
        cell._canvas.delete(const.ALL)
        
        if(piece == Piece.WHITE):   
            cell._canvas.create_oval(10, 10, 50, 50, fill="light grey")
        elif(piece == Piece.BLACK):
            cell._canvas.create_oval(10, 10, 50, 50, fill="black")

    def click_empty(self, event) -> None:
        row = event.widget.master.row
        col = event.widget.master.col
        try:
            self.game.make_move(row + 1, col + 1)
        except InvalidMoveException as e:
            # TODO:
            #  make this print the handled exception's message so we can get rid of
            #  this hard coded string and make it so the error message only has to
            #  be changed in one place
            self._info_label["foreground"] = ["red", "orange", "yellow", "green", "blue", "purple"][randint(0,5)]
            self._info_label["text"] = str(e)
            
        self.refresh_board()

    def start(self) -> None:
        self._root.mainloop()

class ConfigureGUI:

    def __init__(self):
        #
        # Main application window
        #
        self._root = Tk()
        self._root.title("Othello")
        self._root.focus()
        self._root.minsize(400, 250)
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(1, weight=1)
        
        #
        # Welcome label
        #
        welcome_frame = ttk.Frame(self._root, borderwidth=5)
        welcome_label = ttk.Label(welcome_frame, text="Welcome to GUI Othello!")
        
        welcome_frame.grid(row=0, column=0, sticky="ew")
        welcome_label.grid(row=0, column=0, padx=5, pady=5)
        
        welcome_frame.columnconfigure(0, weight=1)
        
        #
        # Main content (Configuration)
        #
        self._content = ttk.Frame(self._root)
        
        self._row = IntVar()
        row_label = ttk.Label(self._content, text="Number of Rows: ")
        row_picker = ttk.Combobox(self._content, state="readonly", textvariable=self._row, values=[4, 6, 8, 10, 12, 14, 16])
        row_picker.set(8)
        
        self._col = IntVar()
        col_label = ttk.Label(self._content, text="Number of Columns: ")
        col_picker = ttk.Combobox(self._content, state="readonly", textvariable=self._col, values=[4, 6, 8, 10, 12, 14, 16])
        col_picker.set(8)
        
        self._white_starts = BooleanVar()
        white_starts_label = ttk.Label(self._content, text="White starts: ")
        white_starts_picker = ttk.Combobox(self._content, state="readonly", textvariable=self._white_starts, values=[True, False])
        white_starts_picker.current(1)
        
        self._classic_board_str = StringVar()
        classic_board_str_label = ttk.Label(self._content, text="Opening Board Style: ")
        classic_board_str_picker = ttk.Combobox(self._content, state="readonly", textvariable=self._classic_board_str)
        classic_board_str_picker["values"] = ["Classic (white starts in the top left)", "Inverted (black starts in the top left)"]
        classic_board_str_picker.set("Classic (white starts in the top left)")
        
        self._most_wins = BooleanVar()
        most_wins_label = ttk.Label(self._content, text="Most Pieces Wins: ")
        most_wins_picker = ttk.Combobox(self._content, state="readonly", textvariable=self._most_wins, values=[True, False])
        most_wins_picker.current(0)

        self._content.grid(row=1, column=0, sticky="nsew")
        
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
        play = ttk.Button(play_frame, text="Play", command=self._press_play)
        cancel = ttk.Button(play_frame, text="Quit", command=exit)
        
        play_frame.grid(row=2, column=0, sticky="nsew")
        play.grid(row=0, column=0, sticky=(const.N, const.S, const.E), padx=5, pady=2)
        cancel.grid(row=0, column=1, sticky=(const.N, const.S, const.W), padx=5, pady=2)
        
        play_frame.columnconfigure(0, weight=1)
        play_frame.columnconfigure(1, weight=1)

    def _press_play(self):
        self._root.destroy()
        self.play = True

    def start(self) -> None:
        self._root.mainloop()
        if not self.play:
            exit()

    def getOthello(self) -> Othello:
        return Othello(self._row.get(), self._col.get(), self._white_starts.get(), True if (self._classic_board_str.get() == "Classic (white starts in the top left)") else False, self._most_wins.get())       

if __name__ == '__main__':
    app = OthelloGUI()
    app.start()
