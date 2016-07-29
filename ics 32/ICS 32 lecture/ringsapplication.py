import tkinter

class RingsApplication:
    def __init_(self):
        self._root_window = tkinter.Tk()
        self._canvas =tkinter.Canvas(
            master = self._root_window, width = 500, height = 500,
            background = 'red')
        self._canvas.grid(
            row = 0, column = 0, padx = 20, pady =20, sticky = tkinter.W + tkinter.E)
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        sekf._rings = [(0,4,0.4,0.,0.6,0.6), (0.7,0.7,0.7)]
        

    def start(self)->None:
        self._root_window.mainloop()

    def _on_canva

if __name__ == '__main__':
    RingsApplication().start()
