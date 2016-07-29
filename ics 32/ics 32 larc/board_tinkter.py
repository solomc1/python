import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(master = root,
                        height = 600,
                        width = 600,
                        background = 'black')

columns = 6
rows = 6

def rect_click(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    obj = canvas.find_closest(x,y)[0]
    tags = canvas.gettags(obj)
    print('Column: ' + tags[0] + ' Row: ' + tags[1])
    
def create_board():
    canvas.delete(tkinter.ALL)
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    for c in range(columns):
        for r in range(rows):
            x1 = c * (width/columns)
            y1 = r * (height/rows)
            x2 = (c+1) * (width/columns)
            y2 = (r+1) * (height/rows)
            rect = canvas.create_rectangle(x1,y1,
                                           x2,y2,
                                           fill = 'blue',
                                           outline = 'white',
                                           tag = (c+1, r+1))
            canvas.tag_bind(rect, '<ButtonPress-1>', rect_click)
                                        
    

def update(event):
    create_board()

canvas.bind('<Configure>', update)
canvas.pack(fill = tkinter.BOTH, expand = tkinter.YES)
root.mainloop()
