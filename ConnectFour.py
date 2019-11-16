class ConnectFour:
    def __init__(self, columns = 7, rows = 6, player1 = 'X', player2 = 'O'):
        self.size = {'c' : columns, 'r': rows} # 7 columns x 6 rows
        self.grid = []
        self.first_player = True # True - player 1 on the move, False - player 2 on the move
        self.players = {True : player1, False : player2} # Anything except ? (question mark) AND 1 character only!
        self.game_over = False
        self.grid = [[] for i in range(self.size['c'])]

    # Returns True if disc was successfully dropped, False otherwise
    def drop(self, column): # Drop a disc into a column
        if self.game_over: return False # Cannot proceed because game has already ended.
        
        if column < 0 or column >= self.size['c']:
            return False
        if len(self.grid[column]) >= self.size['r']:
            return False

        self.grid[column].append(self.players[self.first_player])

        c = self.check()
        if c == False:
            self.first_player = not self.first_player
            return True
        else:
            self.game_over = c
            return True

        
    # Returns False - meaning game is on OR 'win'/'draw' meaning game is over.
    def check(self): # Check whether player has won or forced draw.
        d = 0 # Number of discs
        for i, column in enumerate(self.grid):
            d += len(self.grid[i])
            for j, row in enumerate(column):
                h = i + 4 <= self.size['c'] # Nismo v eni izmed zadnjih štirih stolpcev
                v = j + 4 <= len(self.grid[i]) # V tem stolpcu obstajajo vsaj štiri vrstice
                
                if v: # Check vertically (four fields to the right)
                    if 1 == len(set(self.grid[i][j:j+4])):
                        return 'win'
                    
                if h: # Check horizontally (four fields up)
                    if len(self.grid[i]) > j and len(self.grid[i+1]) > j and len(self.grid[i+2]) > j and len(self.grid[i+3]) > j: 
                        s_r = set()
                        for k in range(4):
                            s_r.add(self.grid[i+k][j])
                        if 1 == len(s_r):
                            return 'win'
                            
                if h: # Check diagonally (up-right)
                    s = set()
                    for k in range(4):
                        if len(self.grid[i+k]) > j + k:
                            s.add(self.grid[i+k][j+k])
                        else:
                            s.add('??')
                    if 1 == len(s):
                        return 'win'
                    
                if h and j - 4 + 1 >= 0: # Check diagonally (down-right)
                # j - 4 + 1 > 0 : Začne se naj komaj v 4. stolpcu (ki ima indeks 3)
                    s = set()
                    for k in range(4):
                        if len(self.grid[i+k]) > j - k:
                            s.add(self.grid[i+k][j-k])
                        else:
                            s.add('??')
                    if 1 == len(s):
                        return 'win'

        if d == self.size['c']*self.size['r']:
            return 'draw'
        
        return False
