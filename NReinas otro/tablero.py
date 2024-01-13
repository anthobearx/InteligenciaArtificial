import tkinter as tk

class ChessboardGUI:
    def __init__(self, size, reinas_list):
        self.size = size
        self.reinas_list = reinas_list
        self.root = tk.Tk()
        self.root.title('N Reinas')
        self.root.geometry('1000x1000')
        self.cuadro_size = min(60, 600 // self.size)  # ajustar el tamaño de las casillas
        self.board_size = self.cuadro_size * self.size
        self.canvas = tk.Canvas(self.root, width=self.board_size, height=self.board_size)
        self.canvas.pack()
        self.draw_board()
        self.root.after(0, self.draw_reinas)
        self.root.mainloop()

    def draw_board(self):
        for row in range(self.size):
            for col in range(self.size):
                x1, y1 = col * self.cuadro_size, row * self.cuadro_size
                x2, y2 = x1 + self.cuadro_size, y1 + self.cuadro_size
                color = 'white' if (row + col) % 2 == 0 else 'gray'
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def draw_reinas(self, index=0):
        if index < len(self.reinas_list):
            self.canvas.delete('all')  
            self.draw_board()
            self.reinas = self.reinas_list[index]
            for row, col in enumerate(self.reinas):
                y = col * self.cuadro_size + self.cuadro_size // 2
                x = row * self.cuadro_size + self.cuadro_size // 2
                self.canvas.create_oval(x - self.cuadro_size // 4, y - self.cuadro_size // 4,
                                        x + self.cuadro_size // 4, y + self.cuadro_size // 4,
                                        fill='black')
            self.root.after(50, self.draw_reinas, index+1)