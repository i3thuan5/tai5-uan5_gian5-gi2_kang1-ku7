# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class 文字辭典(metaclass = ABCMeta):
	_上濟字數 = None
	def 上濟字數(self):
		return self._上濟字數
	# 消警告用
	頂層 = ABCMeta
	@abstractmethod
	def 加詞(self, 詞物件):
		pass
	@abstractmethod
	def 查詞(self, 詞物件):
		pass
