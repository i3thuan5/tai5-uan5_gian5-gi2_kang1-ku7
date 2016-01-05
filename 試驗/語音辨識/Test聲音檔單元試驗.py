from os.path import dirname, abspath, join
from unittest.case import TestCase
from unittest.mock import MagicMock
from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔
from 臺灣言語工具.語音辨識.恬音判斷 import 恬音判斷


class 聲音檔單元試驗(TestCase):

    def setUp(self):
        這馬所在 = dirname(abspath(__file__))
        音檔目錄 = join(這馬所在, '音檔')
        self.音檔所在 = join(音檔目錄, '我.wav')
        self.原始檔所在 = join(音檔目錄, '我.raw')

    def test_讀檔(self):
        聲音檔.對檔案讀(self.音檔所在)

    def test_提掉頭前表(self):
        with open(self.音檔所在, 'rb') as 音:
            音檔 = 聲音檔.對資料轉(音.read())
        with open(self.原始檔所在, 'rb') as 原始:
            self.assertEqual(音檔.wav音值資料(), 原始.read())

    def test_加起哩頭前表(self):
        with open(self.原始檔所在, 'rb') as 原始:
            音檔 = 聲音檔.對參數轉(2, 16000, 1, 原始.read())
        with open(self.音檔所在, 'rb') as 音:
            self.assertEqual(音檔.wav格式資料(), 音.read())

    def test_音框(self):
        # 1.615秒
        音檔 = 聲音檔.對檔案讀(self.音檔所在)
        self.assertEqual(len(list(音檔.全部音框(音框秒數=0.02))), 81)

    def test_切音檔愛切佇中央(self):
        音檔 = 聲音檔.對檔案讀(self.音檔所在)
        回傳結果 = MagicMock()
        回傳結果.side_effect = [
            False, False, True, True, True, False, False, True, False
        ]
        細音檔陣列 = 音檔.照函式切音(回傳結果, 音框秒數=0.2)
        self.assertEqual(len(細音檔陣列), 2)
        # 0.0 1.2
        self.assertEqual(細音檔陣列[0].時間長度(), 1.2)
        # 1.2 1.615
        self.assertEqual(細音檔陣列[1].時間長度(), 0.415)

    def test_切音檔愛切佇三個中央(self):
        音檔 = 聲音檔.對檔案讀(self.音檔所在)
        回傳結果 = MagicMock()
        回傳結果.side_effect = [
            False, True, True, False, False, False, True, True, False
        ]
        細音檔陣列 = 音檔.照函式切音(回傳結果, 音框秒數=0.2)
        self.assertEqual(len(細音檔陣列), 2)
        # 0.0, 0.9
        self.assertEqual(細音檔陣列[0].時間長度(), 0.9)
        # 0.9, 1.1
        self.assertEqual(細音檔陣列[1].時間長度(), 0.715)

    def test_切音檔頭尾嘛愛愛切(self):
        音檔 = 聲音檔.對檔案讀(self.音檔所在)
        回傳結果 = MagicMock()
        回傳結果.side_effect = [
            True, True, True, False, False, True, True, True, True
        ]
        細音檔陣列 = 音檔.照函式切音(回傳結果, 音框秒數=0.2)
        self.assertEqual(len(細音檔陣列), 2)
        # 0.0, 0.8
        self.assertEqual(細音檔陣列[0].時間長度(), 0.8)
        # 0.8, 1.1
        self.assertEqual(細音檔陣列[1].時間長度(), 0.815)

    def test_恬音判斷切音檔(self):
        音檔 = 聲音檔.對檔案讀(self.音檔所在)

        def 有音無(音框):
            特徵 = 恬音判斷.算特徵參數(音框)
            return 特徵['平方平均'] >= 1200000.0 and 特徵['過零機率'] < 0.25 and 特徵['相關係數'] > 0.90

        細音檔陣列 = 音檔.照函式切音(有音無)
        self.assertEqual(len(細音檔陣列), 5)
