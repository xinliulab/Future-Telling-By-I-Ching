 # -*- coding: utf-8 -*-
import random
import numpy
from calculate import Calculate

class SingleChange():

	def __init__(self):
		self.num = 0

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

	# 这三道流程算完，最后的得数只有四种情况：24、28、32、36。无论得出这4个数字中得哪一个，都把这个数字除以4
	# 算出的结果，得出一个爻。（爻是卦的最基本的构成单位）
	# 此答案需记在纸上。（6、7、8、9四种结果之一）
	def quarter(self, array):
		val = len(array)/4
		return val


class TrebleChange():

	def __init__(self):
		self.num = 0

	def change(self, array):
		SC = SingleChange()
		Weed1 = SC.change(array)
		Weed2 = SC.change(Weed1)
		Weed3 = SC.change(Weed2)
		return SC.quarter(Weed3)

# 接着，把所有的49颗棋子重新归拢到一起，重复上述“三变”
# 一个完整的卦由6个爻组成
# 因此在算卦之时，耐心和时间尤为重要
# 我们把六次算出的爻，由下向上分别记录
class Hexagram():
	def __init__(self):
		self.num = 0

	def hexgram(self):
		array = []
		Cal = Calculate()
		TC = TrebleChange()
		Weed1 = Cal.weed(49)		
		array.append(TC.change(Weed1))
		Weed2 = Cal.weed(49)		
		array.append(TC.change(Weed2))
		Weed3 = Cal.weed(49)		
		array.append(TC.change(Weed3))
		Weed4 = Cal.weed(49)		
		array.append(TC.change(Weed4))
		Weed5 = Cal.weed(49)		
		array.append(TC.change(Weed5))
		Weed6 = Cal.weed(49)		
		array.append(TC.change(Weed6))
		return array


