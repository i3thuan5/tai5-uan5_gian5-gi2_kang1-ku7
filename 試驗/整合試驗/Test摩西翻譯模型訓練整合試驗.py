# -*- coding: utf-8 -*-
import os
from unittest.case import TestCase


from 臺灣言語工具.翻譯.摩西工具.摩西翻譯模型訓練 import 摩西翻譯模型訓練
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.翻譯.摩西工具.斷詞轉斷字的編碼器 import 斷詞轉斷字編碼器

class 摩西翻譯模型訓練整合試驗(TestCase):
	def setUp(self):
		這馬目錄=os.path.dirname(os.path.abspath(__file__))
		資料目錄=os.path.join(這馬目錄,'翻譯語料')
		self.平行華語 = [os.path.join(資料目錄,'華'), ]
		self.平行閩南語 = [os.path.join(資料目錄,'閩'), ]
		self.閩南語語料 = [os.path.join(資料目錄,'閩'), ]
	def test_單一模型訓練(self):
		模型訓練 = 摩西翻譯模型訓練()
		模型訓練.訓練(
				self.平行華語, self.平行閩南語, self.閩南語語料,
				os.path.join(os.path.dirname(os.path.abspath(__file__)), '模型資料'),
				連紲詞長度=2,
				編碼器=語句編碼器(),
				SRILM執行檔路徑='/home/tshau/git/mosesdecoder-depth1',
				GIZA執行檔路徑='/home/tshau/git/mgiza/mgizapp/bin',
				MOSES腳本路徑='/home/tshau/git/mosesdecoder-depth1/scripts/',
			)
	def test_訓練摩西斷詞佮斷字模型(self):
		模型訓練 = 摩西翻譯模型訓練()
		這馬資料夾 = os.path.dirname(os.path.abspath(__file__))
		斷詞暫存資料夾 = os.path.join(這馬資料夾, '斷詞模型資料')
		模型訓練.訓練(
				self.平行華語, self.平行閩南語, self.閩南語語料,
				斷詞暫存資料夾,
				連紲詞長度=2,
				編碼器=語句編碼器(),
				SRILM執行檔路徑='/home/tshau/git/mosesdecoder-depth1',
				GIZA執行檔路徑='/home/tshau/git/mgiza/mgizapp/bin',
				MOSES腳本路徑='/home/tshau/git/mosesdecoder-depth1/scripts/',
			)
	
		斷詞編碼器 = 斷詞轉斷字編碼器()
		斷字暫存資料夾 = os.path.join(這馬資料夾, '斷字模型資料')
		模型訓練.訓練(
				self.平行華語, self.平行閩南語, self.閩南語語料,
				斷字暫存資料夾,
				連紲詞長度=2,
				編碼器=斷詞編碼器(),
				SRILM執行檔路徑='/home/tshau/git/mosesdecoder-depth1',
				GIZA執行檔路徑='/home/tshau/git/mgiza/mgizapp/bin',
				MOSES腳本路徑='/home/tshau/git/mosesdecoder-depth1/scripts/',
			)
