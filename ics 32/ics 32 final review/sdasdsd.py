import random
import tkinter

class App:
    def __init__(self):
        self._root = tkinter.Tk()
        self._canvas = tkinter.Canvas(master = self._root, width = 500,
                                      height = 500, background = '#000000')
        self._canvas.grid(row = 0, column = 0, padx = 10, pady = 10)
        self._previous = []
        self._current = '#000000'
        self._canvas.bind('<Button-1>', self._on_left_click)
        self._canvas.bind('<Button-3>', self._on_right_click)

    def start(self):
        self._root.mainloop()

    def _on_left_click(self, event):
        self._previous.append(self._current)
        ran = '#'
        for x in range(6):
            ran += str(random.randrange(9))
        self._current = ran
        self._canvas = tkinter.Canvas(self._root, width = 500, height = 500,
                                      background = ran)
        self._canvas.grid(row = 0, column = 0, padx = 10, pady = 10)
        self._canvas.bind('<Button-1>', self._on_left_click)
        self._canvas.bind('<Button-3>', self._on_right_click)

    def _on_right_click(self, event):
        if len(self._previous) == 0:
            self._current = '#000000'

        else:
            self._current = self._previous[-1]
            self._previous.pop()
        print(self._current)
        self._canvas = tkinter.Canvas(master = self._root, width = 500, height = 500,
                                      background= self._current)
        self._canvas.grid(row = 0, column = 0, padx = 10, pady = 10)
        self._canvas.bind('<Button-1>', self._on_left_click)
        self._canvas.bind('<Button-3>', self._on_right_click)

x = App()
x.start()





#http://domain:port/resources



class exampleclass:
    def __init__(self, n: int):
        self._n = n
        
    def add(self, n: int) -> int:
        return self._n + 6



a = exampleclass(6)

print(a.add(5))
print(exampleclass.add(a, 5))

import socket

HOST = 'evil-monkey.ics.uci.edu'
port = 4444

s = socket.socket()
s.connect((HOST, port))











