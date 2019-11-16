#! /usr/bin/env python3

from tkinter import *
from ConnectFour import ConnectFour
from RLAgent import RLAgent

class GUI:
    elementSize = 50
    gridBorder = 3
    gridColor = "#AAA"
    p1Color = "#4096EE"
    p2Color = "#FF1A00"
    backgroundColor = "#FFFFFF"
    gameOn = False
    
    def __init__(self, master):
        self.master = master
        self.rl_agent = RLAgent()

        master.title('Connect Four')
        
        label = Label(master, text="Connect Four")
        label.grid(row=0)

        button = Button(master, text="New Game!", command=self._newGameButton)
        button.grid(row=1)
        
        self.canvas = Canvas(master, width=200, height=50, background=self.backgroundColor, highlightthickness=0)
        self.canvas.grid(row=2)

        self.currentPlayerVar = StringVar(self.master, value="")
        self.currentPlayerLabel = Label(self.master, textvariable=self.currentPlayerVar, anchor=W)
        self.currentPlayerLabel.grid(row=3)

        self.canvas.bind('<Button-1>', self._canvasClick)
        self.newGame()

    def draw(self):       
        for c in range(self.game.size['c']):
            for r in range(self.game.size['r']):
                if r >= len(self.game.grid[c]): continue
                
                x0 = c*self.elementSize
                y0 = r*self.elementSize
                x1 = (c+1)*self.elementSize
                y1 = (r+1)*self.elementSize
                fill = self.p1Color if self.game.grid[c][r] == self.game.players[True] else self.p2Color
                self.canvas.create_oval(x0 + 2,
                                        self.canvas.winfo_height() - (y0 + 2),
                                        x1 - 2,
                                        self.canvas.winfo_height() - (y1 - 2),
                                        fill = fill, outline=self.gridColor)

    def drawGrid(self):
        x0, x1 = 0, self.canvas.winfo_width()
        for r in range(1, self.game.size['r']):
            y = r*self.elementSize
            self.canvas.create_line(x0, y, x1, y, fill=self.gridColor)

        y0, y1 = 0, self.canvas.winfo_height()
        for c in range(1, self.game.size['c']):
            x = c*self.elementSize
            self.canvas.create_line(x, y0, x, y1, fill=self.gridColor)

    def drop(self, column):
        return self.game.drop(column)

    def newGame(self):
        # Ask for players' names
        self.p1 = 'Blue'
        self.p2 = 'Red'

        # Ask for grid size
        columns = 7
        rows = 6
        
        self.game = ConnectFour(columns=columns, rows=rows)

        self.canvas.delete(ALL)
        self.canvas.config(width=(self.elementSize)*self.game.size['c'],
                           height=(self.elementSize)*self.game.size['r'])
        self.master.update() # Rerender window
        self.drawGrid()
        self.draw()

        self._updateCurrentPlayer()

        self.gameOn = True

    def _updateCurrentPlayer(self):
        p = self.p1 if self.game.first_player else self.p2
        self.currentPlayerVar.set('Current player: ' + p)
        print("current player:", p)
        if p == self.p1:
            new_move = self.rl_agent.update()
            print("THIS IS AI MOVE: ", new_move)
            self.drop(new_move)
            self.draw()
            self.currentPlayerVar.set('Current player: ' + self.p2)
            if self.game.game_over:
                x = self.canvas.winfo_width() // 2
                y = self.canvas.winfo_height() // 2
                if self.game.game_over == 'draw':
                    t = 'DRAW!'
                else:
                    winner = self.p1 if self.game.first_player else self.p2
                    t = winner + ' won!'
                self.canvas.create_text(x, y, text=t, font=("Helvetica", 32), fill="#333")


    def _canvasClick(self, event):
        if not self.gameOn: return
        if self.game.game_over: return
        
        c = event.x // self.elementSize
        if (0 <= c < self.game.size['c']):
            self.drop(c)
            self.rl_agent.update(c)
            self.draw()
            self._updateCurrentPlayer()

        if self.game.game_over:
            x = self.canvas.winfo_width() // 2
            y = self.canvas.winfo_height() // 2
            if self.game.game_over == 'draw':
                t = 'DRAW!'
            else:
                winner = self.p1 if self.game.first_player else self.p2
                t = winner + ' won!'
            self.canvas.create_text(x, y, text=t, font=("Helvetica", 32), fill="#333")

    def _newGameButton(self):
        self.newGame()

root = Tk()
app = GUI(root)

root.mainloop()
