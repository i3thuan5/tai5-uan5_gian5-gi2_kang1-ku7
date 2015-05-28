# -*- coding: utf-8 -*-
from unittest.case import TestCase
import os
from 臺灣言語工具.語音辨識.模型訓練 import 模型訓練

class 加短恬試驗(TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test_加短恬(self):
		模型 = 模型訓練()
		這馬目錄 = os.path.dirname(os.path.abspath(__file__))
		無短恬的模型 = os.path.join(這馬目錄, '試料', '無短恬的模型')
		試加短恬的模型 = os.path.join(這馬目錄, '試料', '試加短恬的模型')
		加短恬的模型 = os.path.join(這馬目錄, '試料', '加短恬的模型')
		模型.模型加短恬(無短恬的模型, 試加短恬的模型)
		self.assertEqual(模型._讀檔案(試加短恬的模型),
			模型._讀檔案(加短恬的模型))
		os.remove(試加短恬的模型)
