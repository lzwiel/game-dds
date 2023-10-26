import tkinter as tk
from random import randint

class MoleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("打地鼠游戏")
        
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        
        self.score = 0
        self.score_label = tk.Label(self.master, text="分数: 0")
        self.score_label.pack()
        
        self.mole = None
        self.start_game()
        
    def start_game(self):
        self.mole = self.create_mole()
        self.canvas.bind("<Button-1>", self.hit_mole)
        self.update_score()
        
    def create_mole(self):
        x = randint(50, 350)
        y = randint(50, 350)
        radius = 20
        mole = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="brown")
        return mole
    
    def hit_mole(self, event):
        x, y = event.x, event.y
        items = self.canvas.find_overlapping(x, y, x, y)
        if self.mole in items:
            self.canvas.delete(self.mole)
            self.score += 1
            self.update_score()
            self.mole = self.create_mole()
            
    def update_score(self):
        self.score_label.config(text=f"分数: {self.score}")

root = tk.Tk()
game = MoleGame(root)
root.mainloop()
运行这段代码，会弹出一个窗口，里面有一个空白的画布和一个分数标签。点击鼠标左键，如果命中地鼠，分数会增加，并且地鼠会在画布上随机位置重新出现。你可以根据需要修改代码以实现更丰富的游戏功能。
