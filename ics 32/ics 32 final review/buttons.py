import tkinter

root = tkinter.Tk()
a = tkinter.Button(root, text = 'Button 1')
a.grid(row = 0, column = 0)

b = tkinter.Button(root, text = 'Button 2')
b.grid(row = 0, column = 1)

c = tkinter.Button(root, text = 'Button 3')
c.grid(row = 1, column = 0)

d = tkinter.Button(root, text = 'Button 4')
d.grid(row = 1, column = 1)

root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 5)

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 5) 

root.mainloop()
