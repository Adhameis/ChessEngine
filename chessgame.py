from tkinter import *

ROWS = 8
COLUMNS = 8


class pieces():
    def __init__(self,color,x,y):
        self.color = color
        self.coordinates = [x,y]
    def Move(self,x,y):
        self.coordinates = [x,y]



class Queen(pieces):
    def __init__(self,color,x,y):
        super().__init__(color,x,y)



class King(pieces):
    def __init__(self,color,x,y):
          super().__init__(color,x,y)



class pawn(pieces):
    def __init__(self,color,x,y):
        super().__init__(color,x,y)



class bishop(pieces): 
    def __init__(self,color,x,y):
        super().__init__(color,x,y)




class knight(pieces): 
    def __init__(self,color,x,y):
        super().__init__(color,x,y)



class rook(pieces): 
    def __init__(self,color,x,y):
        super().__init__(color,x,y)



def setup_pieces():
    pieces_on_board = []

    pieces_on_board.append(rook('black', 1, 1))
    pieces_on_board.append(knight('black', 2, 1))
    pieces_on_board.append(bishop('black', 3, 1))
    pieces_on_board.append(Queen('black', 4, 1))
    pieces_on_board.append(King('black', 5, 1))
    pieces_on_board.append(bishop('black', 6, 1))
    pieces_on_board.append(knight('black', 7, 1))
    pieces_on_board.append(rook('black', 8, 1))


    pieces_on_board.append(rook('white', 1, 8))
    pieces_on_board.append(knight('white', 2, 8))
    pieces_on_board.append(bishop('white', 3, 8))
    pieces_on_board.append(Queen('white', 4, 8))
    pieces_on_board.append(King('white', 5, 8))
    pieces_on_board.append(bishop('white', 6, 8))
    pieces_on_board.append(knight('white', 7, 8))
    pieces_on_board.append(rook('white', 8, 8))

    for i in range(1,9):
        pieces_on_board.append(pawn('white',i,7))
        pieces_on_board.append(pawn('black',i,2))
    for p in pieces_on_board:
        label = Label(window,text=p.coordinates,fg=p.color)
        label.grid(column=int(p.coordinates[0])-1,row=int(p.coordinates[1])-1)


def draw_board():
    for row in range(ROWS):
        for column in range(COLUMNS):
            if (row + column) % 2 == 0:
                color='grey'
            else:
                color="black"

            canvas = Canvas(window,bg=color,width=80,height=80)
            canvas.grid(row=row,column=column)
    setup_pieces()

window = Tk()
window.geometry('640x640')
window.config(background='white')
draw_board()

window.mainloop()
