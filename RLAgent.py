from Arena import Arena
from MCTS import MCTS
from Connect4Game import Connect4Game as Game, display
from Connect4Players import *
from NNet import NNetWrapper as NNet

import numpy as np
from utils import *

class RLAgent:
	def __init__(self):
		g = Game()

		self.hp = HumanConnect4Player(g)
		self.hp_f = self.hp.play

		# nnet players
		n1 = NNet(g)
		n1.load_checkpoint('./data/','best.pth.tar')
		args1 = dotdict({'numMCTSSims': 200, 'cpuct':0})
		mcts1 = MCTS(g, n1, args1)
		n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

		self.arena = Arena(n1p, self.hp_f, g, display=display) # CHANGE THIS TO MAKE AI GO FIRST

	def update(self, action=-1):
		print('Action:', action)
		if action != -1:
			self.arena.playGame(action=action, verbose=True)
		else:
			action = self.arena.playGame(verbose=True)[1]
		return action