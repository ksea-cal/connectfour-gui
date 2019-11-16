from ConnectFourText import ConnectFourText

g = ConnectFourText()

# Test cases

''' Draw
for i in range(6): g.drop(0)
for i in range(6): g.drop(1)
for i in range(6): g.drop(6)
for i in range(5): g.drop(5)
for i in range(6): g.drop(2)
for i in range(6): g.drop(3)
for i in range(6): g.drop(4)
g.drop(5)
#'''

''' Player 1 wins vertically
for i in range(3): g.drop(1); g.drop(2);
g.drop(1)
#'''

''' Player 2 wins horizontally
for i in range(3): g.drop(1+i); g.drop(1+i);
g.drop(5)
g.drop(4)
g.drop(5)
g.drop(4)
#'''

''' Player 1 wins diagonally (up-right)
g.drop(0)
g.drop(1); g.drop(1)
g.drop(2); g.drop(3); g.drop(2); g.drop(2)
g.drop(3); g.drop(4); g.drop(3); g.drop(3)
#'''

''' Player 1 wins diagonally (up-right) #2
g.drop(0); g.drop(1); g.drop(2); g.drop(3); g.drop(4); g.drop(5);
g.drop(0); g.drop(1); g.drop(2); g.drop(3); g.drop(4); g.drop(5);
g.drop(2+0)
g.drop(2+1); g.drop(2+1)
g.drop(2+2); g.drop(2+3); g.drop(2+2); g.drop(2+2)
g.drop(2+3); g.drop(2+4); g.drop(2+3); g.drop(2+3)
#'''

''' Player 1 wins diagonally (down-right)
g.drop(0); g.drop(0); g.drop(3); g.drop(0); g.drop(0);
g.drop(6);
g.drop(1); g.drop(1); g.drop(1); g.drop(2); g.drop(2)
#'''
