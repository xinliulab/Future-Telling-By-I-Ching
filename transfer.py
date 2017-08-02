# -*- coding: utf-8 -*-
import random
import numpy
from change import Hexagram as Hex
from iching import IChing as IC

class Transfer():

	def __init__(self):
		self.num = 0

	# 我们先给“6、7、8、9”分阴阳：7、9都是奇数，为“阳”；6和8都是偶数，叫“阴”
	# 不止这么简单，还需继续分：6是老阴，8是少阴，7是少阳，9是老阳
	# 以四分法来看，这一卦是：“少阴、少阴、老阴、老阳、少阴、少阳”（8、8、6、9、8、8）
	# 呈现“豫卦”
	def yinYangTransfer(self, array):
		newArray = []
		for i in range (len(array)):
			if array[i]%2 == 1:
				newArray.append(1)
			else:
				newArray.append(0)
		return newArray

	# 现在还需要在豫卦的基础上变出一个新卦，这就是谦卦。（遵循的原理：老变少不变）。
	# 此时，豫卦为本卦，谦卦为变卦
	def shaoTaiTransfer(self, array):
		newArray = []
		for i in range (len(array)):
			if array[i] == 6:
				newArray.append(9)
			elif array[i] == 9:
				newArray.append(6)
			else:
				newArray.append(array[i])
		return self.yinYangTransfer(newArray)

	# 有变卦也有变爻，原本豫卦里从下往上数的第三爻的数字是6，也就是少阴，变为阳爻；
	# 第四爻的数字是9，是老阳，变为阴爻。
	# 演算到这里，得出了变卦和变爻，终于完成了整个占卜
	def yaoTransfer(self, array):
		newArray = []
		newArray = self.yinYangTransfer(array)
		return newArray


# Weed = Cal.weed(49)
# print Weed, len(Weed)

# print TC.change(Weed)

# Weed1 = Cha.change(Weed)
# print Weed1, len(Weed1)

# Weed2 = Cha.change(Weed1)
# print Weed2, len(Weed2)

# Weed3 = Cha.change(Weed2)
# print Weed3, len(Weed3)

# print Cha.quarter(Weed3)