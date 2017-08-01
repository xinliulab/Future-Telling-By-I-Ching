 # -*- coding: utf-8 -*-
import math
import random
import sys
import numpy
	
class Hexagrams():

	def __init__(self):
		self.numWeed = 49 # 取四十九根蓍草
		self.seed = 0
		self.randomList = []
		self.allGroup = []
		self.skyGroup =[]
		self.earthGroup = []

	def randomseed(self, seed):
		self.seed = seed

	def random(self, num):
		preGroup = []

		# random.seed(self.seed)
		for i in range (num):
			self.randomList.append(random.randint(0, 1))


		for i in range (num):
			preGroup.append([i+1, self.randomList[i]])

		for i in range (num):
			if preGroup[i][-1] == 0:
				self.skyGroup.append(preGroup[i])
			else:
				self.earthGroup.append(preGroup[i])

	# 把四十九根蓍草随机分成左右两组，象征着混沌初开，天与地一分为二。两组蓍草，一组象征着天，一组象征着地。
	def group(self, name):
		if name == 'Sky':
			return self.skyGroup
		elif name == 'Earth':
			return self.earthGroup
		elif name == 'All':
			self.allGroup.append(self.skyGroup)
			self.allGroup.append(self.earthGroup)
			return self.allGroup
		else:
			return "No such group"

	# 从任意一组当中拿掉一根蓍草（通常会从象征地的右边一组里拿），这根蓍草象征的就是人。天、地、人，称“三才”
	def reduceOneElement(self, array):
		id = random.sample(numpy.arange(0, len(array), 1), 1)
		array.pop(id[-1])
		return array
		 
	# 把象征天的那组蓍草数数有多少根，数清楚之后把这个数字除以4（4象征一年四季），看看余数是几
	# 任何数字除以4，余数都只有四种可能：1、2、3、整除
	# 如果遇到整除的情况，我们就当做余数是4。好了，现在把余数拿开
	# 把象征地的那组棋子照猫画虎，和“3”的做法一致
	def quarterRemains(self, array):
		remains = len(array) % 4
		if remains == 0 :
			return 4
		else:
			return remains
	
	# 把“2”里用来象征人的那一颗棋子，加上“3”中作为余数被拿掉的棋子，还有“4”里同样作为余数被拿掉的棋子归在一起。
	# 得出的数字只有两种可能：不是9就是5。如果错了，你就从头再来吧。
	def check(self, valS, valE):
		if valS + valE == 4 or valS + valE ==8:
			return "Successful"
		else:
			return "Failure"

	def intergrate(self, arrayS, arrayE):






Hex = Hexagrams()

Hex.random(49)
skyGroup = Hex.group('Sky')
earthGroup = Hex.group('Earth')
print skyGroup, len(skyGroup)
print earthGroup, len(earthGroup)

earthGroup = Hex.reduceOneElement(earthGroup)
print earthGroup, len(earthGroup)

skyRemains = Hex.quarterRemains(skyGroup)
earthRemains = Hex.quarterRemains(earthGroup)

print skyRemains, earthRemains
print Hex.check(skyRemains, earthRemains)


