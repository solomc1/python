import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(master = root,
                        height = 600,
                        width = 600,
                        background = 'pink')

def rect_click(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    obj = canvas.find_closest(x,y)[0]
    tag = canvas.gettags(obj)
    print('Fill: ' + tag[0] + ' Outline: ' + tag[1])

##for i in range(3):
##    rectangle = canvas.create_rectangle(0+200*i,0, 300+200*i, 200,
##                        fill = 'black',
##                        outline = 'red',
##                        width = 5,
##                        tag = ('white,red'))

rect = canvas.create_rectangle(10,0, 30+200, 100,
                        fill = 'white',
                        outline = 'red',
                        width = 5,
                        tag = ('white,red'))

rect2 = canvas.create_rectangle(0+200,0, 300+200, 200,
                        fill = 'green',
                        outline = 'blue',
                        width = 5,
                        tag = ('green,blue'))



canvas.tag_bind(rect, '<ButtonPress-1>', rect_click)
canvas.tag_bind(rect2, '<ButtonPress-1>', rect_click)




canvas.pack()
root.mainloop()



































