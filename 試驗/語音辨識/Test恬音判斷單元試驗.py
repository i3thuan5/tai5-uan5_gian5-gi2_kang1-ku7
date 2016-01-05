from os.path import dirname, abspath, join
from unittest.case import TestCase
from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔
from 臺灣言語工具.語音辨識.恬音判斷 import 恬音判斷


class 恬音判斷單元試驗(TestCase):

    def setUp(self):
        這馬所在 = dirname(abspath(__file__))
        音檔目錄 = join(這馬所在, '音檔')
        self.音檔 = 聲音檔.對檔案讀(join(音檔目錄, '我.wav'))

    def test_特徵(self):
        for 音框 in self.音檔.全部音框():
            參數 = 恬音判斷.算特徵參數(音框)
            self.assertIn('平方平均', 參數)
            self.assertIn('過零機率', 參數)
            self.assertIn('相關係數', 參數)

    def 平方平均(self):
        for 音框 in self.音檔.全部音框():
            平方平均 = 恬音判斷.平方平均(音框)
            self.assertGreaterEqual(平方平均, 0)

    def test_過零機率(self):
        for 音框 in self.音檔.全部音框():
            過零機率 = 恬音判斷.過零機率(音框)
            self.assertGreaterEqual(過零機率, 0)
            self.assertLessEqual(過零機率, 1)

    def test_相關係數(self):
        for 音框 in self.音檔.全部音框():
            相關係數 = 恬音判斷.相關係數(音框)
            self.assertGreaterEqual(相關係數, -1)
            self.assertLessEqual(相關係數, 1)

    def test_攏零算相關係數(self):
        self.assertEqual(恬音判斷.相關係數([0, 0, 0, 0, 0, 0]), None)
