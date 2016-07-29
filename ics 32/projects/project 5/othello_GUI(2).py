#Solomon Chan 40786337

import othello_logic
from tkinter import *
import othello_coordinate

class draw_setup:
    def __init__(self,rows:int, columns):
        self._root_window = Tk()
        self._rows = rows
        self._columns = columns

        

        self._rect_canvas = Canvas(master = self._root_window,
                        height = 600,
                        width = 800,
                        background = 'blue')
        
        self._label = Label(self._root_window, text = "BLACK: "+ "  \t WHITE: Next Player", fg = 'light green',
                              bg = 'dark green',
                              font = "Helvetica 16 bold italic",
                            )        

    def click_rectangle(self,event):
        x = self._rect_canvas.canvasx(event.x)
        y = self._rect_canvas.canvasy(event.y)
        item = self._rect_canvas.find_closest(x,y)[0]
        tags = self._rect_canvas.gettags(item)
        print('Column: ' + tags[0] + ' Row: ' + tags[1])

    def draw_board(self,event):
        self._rect_canvas.delete(ALL)
        width = self._rect_canvas.winfo_width()
        height = self._rect_canvas.winfo_height()
        for col in range(self._columns):
            for row in range(self._rows):
                x1 = col * (width/self._columns)
                y1 = row * (height/self._rows)
                x2 = (col + 1) * (width/self._columns)
                y2 = (row + 1) * (height/self._rows)
                
                rect = self._rect_canvas.create_rectangle(x1, y1,
                                                          x2, y2,
                                                          fill = 'blue',
                                                          outline = 'white',
                                                          tag = (col + 1, row +1))
                self._rect_canvas.tag_bind(rect, '<ButtonPress-1>', self.click_rectangle)

    

##    def when_clicked(self, event)->None:
##        width = self._rect_canvas.winfo_width()
##        height = self._rect_canvas.winfo_height()
##        click_point_xy = othello_coordinate.from_absolute(
##            (event.x, event.y), (width, height))

    def draw_piece(self):
      #  self._rect_canvas.delete(ALL)
        width = self._rect_canvas.winfo_width()
        height = self._rect_canvas.winfo_height()
        
        for col in range(self._columns):
            for row in range(self._rows):
                
                x1 = col * (width/self._columns)
                y1 = row * (height/self._rows)
                x2 = (col + 1) * (width/self._columns)
                y2 = (row + 1) * (height/self._rows)

                self._rect_canvas.create_oval(x1,y1,
                                                      x2,y2,
                                                      fill = 'white')

    def redraw_everything(self,event):
        self.draw_board(event)
        self.draw_piece()
                                                      
        

  
        
                
        
    def start(self)->None:
        self._rect_canvas.bind('<Configure>', self.redraw_everything)
        self._label.pack(side = TOP)
        self._rect_canvas.pack(fill = BOTH, expand = YES)
        
        #self._label.pack(side=LEFT)
        


if __name__ == '__main__':
    draw_setup(6,6).start()

            
                                                


 
##    def draw_top_left(self)-> None:
##        self._rect_canvas.delete(ALL)
##        
##        middle_row = self._rows/2
##        middle_column = self._columns/2
##        
##        top_left_top_left = (middle_row-1,middle_column-1)
##        bottom_left_top_left = (middle_row-1,middle_column)
##        bottom_left_bottom_right = (middle_row,middle_column-1)
##        center = (middle_row, middle_column)
##        bottom_right_bottom_right = (middle_row+1, middle_column+1)
##        bottom_right_top_right = (middle_row+1,middle_column)
##        top_left_top_right = (middle_row,middle_column+1)
##
##        top_left_rect = (top_left_top_left, center)
##        top_right_rect = (top_left_top_right, bottom_right_top_right)
##        bottom_left_rect =(bottom_left_top_left, bottom_left_bottom_right)
##        bottom_right_rect = (center,bottom_right_bottom_right)
##
##        if top_left_rect and bottom_left_rect:
##            x_rad = othello_coordinate.
##
##  
##
##        for spot in self._state.all_spots():
##            center_x, center_y = spot.center_coordinate().absolute(
##                (canvas_width, canvas_height))
##
##            radius_x = spot.radius_frac() * canvas_width
##            radius_y = spot.radius_frac() * canvas_height
##            
##            self._canvas.create_oval(
##                center_x - radius_x, center_y - radius_y,
##                center_x + radius_x, center_y + radius_y,
##                fill = '#ffff00', outline = '#000000')
