# -*- coding: utf-8 -*-
from unittest.case import TestCase


from 臺灣言語工具.語音辨識.文本音值對照表.閩南語文本音值表 import 閩南語文本音值表
from 臺灣言語工具.語音辨識.文本音值對照表.客家話文本音值表 import 客家話文本音值表
from 臺灣言語工具.語音辨識.文本音值對照表.官話文本音值表 import 官話文本音值表


class 文本音值對照表單元試驗(TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_閩南語聲韻表(self):
		文本音值表 = 閩南語文本音值表()	
		聲韻表 = 文本音值表.聲韻表()
		self.assertGreater(len(聲韻表), 80)

	def test_閩南語聲韻對照(self):
		文本音值表 = 閩南語文本音值表()
		對照 = 文本音值表.音節佮聲韻對照()
		self.assertGreater(len(對照), 1000)
		文本音值表.聲韻表()

	def test_客家話聲韻表(self):
		文本音值表 = 客家話文本音值表()
		聲韻表 = 文本音值表.聲韻表()
		self.assertGreater(len(聲韻表), 50)

	def test_客家話聲韻對照(self):
		文本音值表 = 客家話文本音值表()
		對照 = 文本音值表.音節佮聲韻對照()
		self.assertGreater(len(對照), 800)
		文本音值表.聲韻表()

	def test_官話聲韻表(self):
		文本音值表 = 官話文本音值表()
		聲韻表 = 文本音值表.聲韻表()
		self.assertGreater(len(聲韻表), 50)

	def test_官話聲韻對照(self):
		文本音值表 = 官話文本音值表()
		對照 = 文本音值表.音節佮聲韻對照()
		self.assertGreater(len(對照), 400)
		文本音值表.聲韻表()
