 # -*- coding: utf-8 -*-
import math
import random
import sys
import numpy
	
class CalculateHexagrams():

	def __init__(self):
		self.numWeed = 49 # 取四十九根蓍草
		self.seed = 0

	def randomseed(self, seed):
		self.seed = seed

	# 把四十九根蓍草随机分成左右两组，象征着混沌初开，天与地一分为二。两组蓍草，一组象征着天，一组象征着地。
	def group(self, name):
		randomGroup = []
		allGroup = []
		skyGroup = []
		earthGroup = []

		for i in range (self.numWeed):
			randomGroup.append(random.randint(0, 1))

		for i in range (self.numWeed):
			allGroup.append([i+1, randomGroup[i]])

		for i in range (self.numWeed):
			if allGroup[i][-1] == 0:
				skyGroup.append(allGroup[i])
			else:
				earthGroup.append(allGroup[i])

		if name == 'All':
			return allGroup
		elif name == 'Sky':
			return skyGroup
		elif name == 'Earth':
			return earthGroup
		else:
			return "No such group"

	# 从任意一组当中拿掉一根蓍草（通常会从象征地的右边一组里拿），这根蓍草象征的就是人。天、地、人，称“三才”
	def newEarthGroup(self):
		array = self.group('Earth')
		id = random.sample(numpy.arange(0, len(array), 1), 1)
		# print self.earthGroup, id[-1]
		array.pop(id[-1])
		return array

	# 把象征天的那组蓍草数数有多少根，数清楚之后把这个数字除以4（4象征一年四季），看看余数是几
	# 任何数字除以4，余数都只有四种可能：1、2、3、整除
	# 如果遇到整除的情况，我们就当做余数是4。好了，现在把余数拿开
	# 把象征地的那组棋子照猫画虎，和“3”的做法一致
	def quarterGroup(self, array):
		remains = len(array) % 4
		if remains == 4 :
			return 0
		else:
			return remains


sg = CalculateHexagrams()
print sg.quarterGroup(sg.group('Sky'))
print sg.quarterGroup(sg.newEarthGroup())
