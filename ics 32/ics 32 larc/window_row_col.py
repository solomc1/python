import tkinter

class rowcolget:
    def __init__(self):
        self._root = tkinter.Tk()
        self._dialog_window = tkinter.Toplevel(self._root)

        self._row_message = tkinter.Label(self._dialog_window,
                                          text = "Enter a row: ",
                                          font = ('Arial', 30),
                                          fg = 'blue')
        self._row_message.grid(row = 0, column = 0, padx = 20, pady = 10)
        
        self._row_entry = tkinter.Entry(self._dialog_window,
                                        width = 20,
                                        font = ('Arial', 30))
        
        self._row_entry.grid(row = 0, column = 1)

        self._col_message = tkinter.Label(self._dialog_window,
                                          text = "Enter a col: ",
                                          font = ('Arial', 30),
                                          fg = 'blue')
        self._col_message.grid(row = 1, column = 0, padx = 20, pady = 10)
        

        self._col_entry = tkinter.Entry(self._dialog_window,
                                        width = 20,
                                        font = ('Arial', 30))
        
        self._col_entry.grid(row = 1, column = 1)


        self._row_message.grid(row = 0, column = 0, padx = 20, pady = 20)

        self._ok = tkinter.Button(self._dialog_window,
                                  text = 'OK',
                                  font = ('Arial', 30),
                                  command = self._ok_clicked)

        
        self._ok.grid(row = 2, column = 1)

        self._dialog_window.bind('<Return>', self._ok_clicked)

    def _ok_clicked(self,event = None):
        self._columns = self._col_entry.get()
        self._rows = self._row_entry.get()
        self._dialog_window.destroy()
                                  

    def run(self):

        self._root.withdraw()
        self._dialog_window.wait_window()
        self._root.deiconify()

    def col_row(self):
        return (self._columns, self._rows)


rowcol = rowcolget()
rowcol.run()
print(rowcol.col_row())

##partner up and create a class that asks the user to enter a # of rows
## and also columns


