 # -*- coding: utf-8 -*-
import random
import numpy
	
class Calculate():

	def __init__(self):
		self.seed = 0

	def randomseed(self, seed):
		self.seed = seed

	# 1.1: 把四十九根蓍草随机分成左右两组，象征着混沌初开，天与地一分为二
	def weed(self, num):		
		array = []
		for i in range (num):
			array.append([i+1])
		return array

	def random(self, array):
		for i in range (len(array)):
			array[i].extend(random.sample(list(numpy.arange(0, 2, 1)), 1))
		return array

	# 1.1: 两组蓍草，一组象征着天，一组象征着地
	def devide(self, source, obj):
		array = []
		if obj == 0:
			for i in range (len(source)):
				if source[i][-1] == 0:
					array.append(source[i])
			return array
		elif obj == 1:
			for i in range (len(source)):
				if source[i][-1] == 1:
					array.append(source[i])
			return array
		else:
			return "No such group"

	# 1.2: 从任意一组当中拿掉一根蓍草（通常会从象征地的右边一组里拿），这根蓍草象征的就是人。天、地、人，称“三才”
	# 1.3: 把象征天的那组蓍草数数有多少根，数清楚之后把这个数字除以4（4象征一年四季），看看余数是几
	# 1.3: 任何数字除以4，余数都只有四种可能：1、2、3、整除
	# 1.3: 如果遇到整除的情况，我们就当做余数是4。好了，现在把余数拿开
	# 1.4: 把象征地的那组棋子照猫画虎，和“3”的做法一致
	def reduceElement(self, array, operation):
		if operation == 1:
			id = random.sample(list(numpy.arange(0, len(array), 1)), 1)
			array.pop(id[-1])
			return array
		elif operation == 0:
			remains = len(array)%4
			if remains == 0:
				remains = 4
			id = random.sample(list(numpy.arange(0, len(array), 1)), remains)
			id.sort()
			for i in range (len(id)): 
				array.pop(id[i]-i)
			return array
		else:
			return "No such operation"
	
	# 1.5: 把“2”里用来象征人的那一颗棋子，加上“3”中作为余数被拿掉的棋子，还有“4”里同样作为余数被拿掉的棋子归在一起
	# 1.5: 得出的数字只有两种可能：不是9就是5。如果错了，你就从头再来吧
	def quarterRemains(self, array):
		remains = len(array) % 4
		if remains == 0 :
			return 4
		else:
			return remains

	def check(self, valS, valE):
		return valS + valE + 1

	# 2.1: 好了，从1.1-1.5完成动作，叫做“一变”。
	# 2.1: 接着，“二变”开始。
	# 2.1: 把“一变”最后剩余的左右两组棋子重新混到一起，然后再随机分为两组。
	def intergrate(self, arrayS, arrayE):
		newArray = arrayS + arrayE
		return newArray

# s = [[2, 0], [4, 0], [6, 0], [7, 0], [8, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [21, 0], [24, 0], [25, 0], [26, 0], [28, 0], [30, 0], [31, 0], [34, 0], [37, 0], [38, 0], [39, 0], [42, 0], [43, 0], [44, 0], [46, 0], [47, 0]]
# e = [[1, 1], [3, 1], [5, 1], [9, 1], [19, 1], [20, 1], [22, 1], [23, 1], [27, 1], [29, 1], [32, 1], [33, 1], [35, 1], [36, 1], [40, 1], [41, 1], [45, 1], [48, 1]]
# cal = Calculate()
# print cal.check(cal.quarterRemains(s),cal.quarterRemains(e))
# print cal.quarterRemains(e)