 # -*- coding: utf-8 -*-
import random
import numpy
from calculating import Calculate

class Change():

	def __init__(self):
		self.seed = 0

	def change(self, array):
		Cal = Calculate()
		ary = Cal.random(array)
		# print ary
		skyWeed_1_0 = Cal.devide(ary, 0)
		earthWeed_1_0 = Cal.devide(ary, 1)
		# print 's1-0', skyWeed_1_0, len(skyWeed_1_0)
		# print 'e1-0', earthWeed_1_0, len(earthWeed_1_0)

		earthWeed_1_1 = Cal.reduceElement(earthWeed_1_0, 1)
		# print 'e1-1', earthWeed_1_1, len(earthWeed_1_1)

		# print Cal.check(Cal.quarterRemains(skyWeed_1_0), Cal.quarterRemains(earthWeed_1_1))

		skyWeed_1_2 = Cal.reduceElement(skyWeed_1_0, 0)
		earthWeed_1_2 = Cal.reduceElement(earthWeed_1_1, 0)
		# print 's1-1', skyWeed_1_2, len(skyWeed_1_2)
		# print 'e1-1', earthWeed_1_2, len(earthWeed_1_2)

		# 2.2: 和“一变”的“2”一样。
		# 2.3: 和“一变”的“3”一样。
		# 2.4: 和“一变”的“4”一样。
		# 2.5: 和“一变”的“5”一样。
		newWeed = Cal.intergrate(skyWeed_1_2, earthWeed_1_2)
		# print newWeed, len(newWeed)
		return newWeed

Cal = Calculate()
Cha = Change()

Weed = Cal.weed(49)
print Weed, len(Weed)

Weed1 = Cha.change(Weed)
print Weed1, len(Weed1)

Weed2 = Cha.change(Weed1)
print Weed2, len(Weed2)

Weed3 = Cha.change(Weed2)
print Weed3, len(Weed3)

