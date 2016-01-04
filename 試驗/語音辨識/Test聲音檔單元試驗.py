from os.path import dirname, abspath, join
from unittest.case import TestCase
from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔


class 聲音檔單元試驗(TestCase):

    def setUp(self):
        這馬所在 = dirname(abspath(__file__))
        音檔目錄 = join(這馬所在, '音檔')
        self.音檔 = join(音檔目錄, '我.wav')

    def test_讀檔(self):
        聲音檔.從檔案讀(self.音檔)

    def test_音框(self):
        # 1.615秒
        音檔 = 聲音檔.從檔案讀(self.音檔)
        self.assertEqual(len(list(音檔.全部音框())), 9)
