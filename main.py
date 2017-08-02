 # -*- coding: utf-8 -*-
import random
import numpy
from change import Hexagram as Hex
from transfer import Transfer as Tra
from iching import IChing as IC

# 演算到这里，得出了变卦和变爻，终于完成了整个占卜。
# 此时，我们可以用两个变爻的占辞来判断吉凶，定名字；并以位置考上的那一个变爻的占辞为主。
# 参见《易经》，我们可以得到结果：“九四，由豫,大有得;勿疑,朋盍簪。”

class Read():
	def __init__(self):
		self.num = 0

	def read(self):
		index = 0
		array = Hex().hexgram()
		print array
		oldHex = Tra().yinYangTransfer(array)
		print oldHex
		newHex = Tra().shaoTaiTransfer(array)
		print newHex

		for i in range (len(newHex)):
			if newHex[i] != oldHex[i]:
				index = i + 1

		print "第 ", index, " 爻"
		print IC().text(oldHex)
 
Read().read()