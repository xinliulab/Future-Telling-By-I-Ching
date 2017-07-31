 # -*- coding: utf-8 -*-
import math
import random
import sys
import numpy

class SuanGua(): 
	def __init__(self):
		self.numShiCao = 49
		self.ShiCao = [[]] # 取四十九根蓍草
		self.seed = 0

	def randomseed(self, seed):
		self.seed = seed

	# 把四十九颗棋子随机分成左右两组，象征着混沌初开，天与地一分为二。两组棋子，一组象征着天，一组象征着地。
	def array(self):
