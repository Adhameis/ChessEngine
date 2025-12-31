from tkinter import *
from PIL import ImageTk, Image

ROWS = 8
COLUMNS = 8


class pieces():
    def __init__(self,color,x,y, piece_type):
        self.color = color
        self.coordinates = [x,y]
        self.type = piece_type
    def Move(self,x,y):
        self.coordinates = [x,y]



class Queen(pieces):
    def __init__(self,color,x,y):
        super().__init__(color,x,y,'Queen')



class King(pieces):
    def __init__(self,color,x,y):
          super().__init__(color,x,y,'King')



class pawn(pieces):
    def __init__(self,color,x,y):
        super().__init__(color,x,y,'Pawn')



class bishop(pieces): 
    def __init__(self,color,x,y):
        super().__init__(color,x,y,'Bishop')




class knight(pieces): 
    def __init__(self,color,x,y):
        super().__init__(color,x,y,'Knight')



class rook(pieces): 
    def __init__(self,color,x,y):
        super().__init__(color,x,y,'Rook')



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
        if (int(p.coordinates[0]) + int(p.coordinates[1])) % 2 == 0:
            square_color='white'
        else:
            square_color="grey"

        if p.color == 'black':
            c='b'
        else:
            c='w'
        path =f'/home/eyad/Chess_Pieces/{p.type.lower()}-{c}.png'

        og_img = Image.open(path).convert('RGBA')
        resized_img = og_img.resize((80, 80))
        img = ImageTk.PhotoImage(resized_img)
        panel = Label(window, image=img,bg=square_color)
        panel.image = img
        panel.grid(column=int(p.coordinates[0])-1,row=int(p.coordinates[1])-1)


def draw_board():
    for row in range(ROWS):
        for column in range(COLUMNS):
            if (row + column) % 2 == 0:
                color='white'
            else:
                color="grey"

            canvas = Canvas(window,bg=color,width=80,height=80)
            canvas.grid(row=row,column=column)
    setup_pieces()

window = Tk()
window.title('Chess')
window.geometry('640x640')
window.config(background='white')
draw_board()

window.mainloop()
