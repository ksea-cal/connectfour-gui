import numpy as np
import time

class Arena():
    """
    An Arena class where any 2 agents can be pit against each other.
    """
    def __init__(self, player1, player2, game, display=None):
        """
        Input:
            player 1,2: two functions that takes board as input, return action
            game: Game object
            display: a function that takes board as input and prints it (e.g.
                     display in othello/OthelloGame). Is necessary for verbose
                     mode.

        see othello/OthelloPlayers.py for an example. See pit.py for pitting
        human players/other baselines with each other.
        """
        self.player1 = player1
        self.player2 = player2
        self.game = game
        self.display = display
        self.players = [self.player2, None, self.player1]
        self.board = self.game.getInitBoard()
        self.curr_player = 1


    def playGame(self, action=-1, verbose=False):
        """
        Executes one episode of a game.

        Returns:
            either
                winner: player who won the game (1 if player1, -1 if player2)
            or
                draw result returned from the game that is neither 1, -1, nor 0.
        """
        #it = 0
        #print("I'm in PlayGame, I'm player ", self.curr_player)
        if self.game.getGameEnded(self.board, self.curr_player)==0:
            #it+=2
            if verbose:
                assert(self.display)
                #print("Turn ", str(it), "Player ", str(self.curr_player))
                self.display(self.board)
            if action == -1:
                print(self.players[self.curr_player+1])
                action = self.players[self.curr_player+1](self.game.getCanonicalForm(self.board, self.curr_player))
            print("Action:", action)
            valids = self.game.getValidMoves(self.game.getCanonicalForm(self.board, self.curr_player),1)

            if valids[action]==0:
                print(action)
                assert valids[action] >0
            self.board, self.curr_player = self.game.getNextState(self.board, self.curr_player, action) 
        else:
            action = None

        if verbose:
            assert(self.display)
            #print("Game over: Turn ", str(it), "Result ", str(self.game.getGameEnded(self.board, 1)))
            self.display(self.board)
        return self.game.getGameEnded(self.board, 1), action

