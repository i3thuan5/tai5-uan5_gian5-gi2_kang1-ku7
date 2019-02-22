from os.path import dirname, abspath, join
from unittest.case import TestCase
import wave
from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔


class 聲音檔單元試驗(TestCase):

    def setUp(self):
        這馬所在 = dirname(abspath(__file__))
        音檔目錄 = join(這馬所在, '音檔')
        self.音檔所在 = join(音檔目錄, '我.wav')
        self.原始檔所在 = join(音檔目錄, '我.raw')
        'http://wavefilegem.com/how_wave_files_work.html'
        self.format65534所在 = join(音檔目錄, 'format65534.wav')

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

    def test_一般位元組數(self):
        with open(self.原始檔所在, 'rb') as 原始:
            音檔 = 聲音檔.對參數轉(2, 16000, 1, 原始.read())
        self.assertEqual(音檔.一秒位元組數(), 32000)

    def test_錄音位元組數(self):
        with open(self.原始檔所在, 'rb') as 原始:
            音檔 = 聲音檔.對參數轉(2, 44100, 2, 原始.read())
        self.assertEqual(音檔.一秒位元組數(), 176400)

    def test_時間長度(self):
        音檔 = 聲音檔.對參數轉(2, 16000, 1, b'0' * 48000)
        self.assertEqual(音檔.時間長度(), 1.5)

    def test_產生仝參數空音檔(self):
        原本音檔 = 聲音檔.對參數轉(2, 16000, 1, b'0' * 48000)
        空音檔 = 原本音檔.產生仝參數空聲音檔()
        self.assertEqual(空音檔.一點幾位元組, 2)
        self.assertEqual(空音檔.一秒幾點, 16000)
        self.assertEqual(空音檔.幾个聲道, 1)
        self.assertEqual(空音檔.時間長度(), 0)

    def test_接兩音檔(self):
        頭音檔 = 聲音檔.對參數轉(2, 16000, 1, b'0' * 1600)
        尾音檔 = 聲音檔.對參數轉(2, 16000, 1, b'1' * 1600)
        合音檔 = 頭音檔.接(尾音檔)
        self.assertEqual(合音檔.一點幾位元組, 2)
        self.assertEqual(合音檔.一秒幾點, 16000)
        self.assertEqual(合音檔.幾个聲道, 1)
        self.assertEqual(合音檔.wav音值資料(), b'0' * 1600 + b'1' * 1600)

    def test_接三音檔(self):
        頭音檔 = 聲音檔.對參數轉(2, 16000, 1, b'5' * 1600)
        中音檔 = 聲音檔.對參數轉(2, 16000, 1, b'9' * 1600)
        尾音檔 = 聲音檔.對參數轉(2, 16000, 1, b'3' * 1600)
        合音檔 = 頭音檔.接(中音檔.接(尾音檔))
        self.assertEqual(合音檔.一點幾位元組, 2)
        self.assertEqual(合音檔.一秒幾點, 16000)
        self.assertEqual(合音檔.幾个聲道, 1)
        self.assertEqual(
            合音檔.wav音值資料(), b'5' * 1600 + b'9' * 1600 + b'3' * 1600
        )

    def test_接音檔參數無仝(self):
        頭音檔 = 聲音檔.對參數轉(2, 16000, 1, b'0' * 1600)
        尾音檔 = 聲音檔.對參數轉(2, 48000, 1, b'1' * 1600)
        with self.assertRaises(ValueError):
            頭音檔.接(尾音檔)

    def test_接音檔無改著原本音檔(self):
        頭音檔 = 聲音檔.對參數轉(2, 16000, 1, b'0' * 1600)
        尾音檔 = 聲音檔.對參數轉(2, 16000, 1, b'1' * 1600)
        頭音檔.接(尾音檔)
        self.assertEqual(頭音檔.wav音值資料(), b'0' * 1600)
        self.assertEqual(尾音檔.wav音值資料(), b'1' * 1600)

    def test_照秒數切出音檔(self):
        音檔 = 聲音檔.對參數轉(2, 16000, 1, b'0' * 1600 + b'1' * 1600)
        wav音值資料 = 音檔.照秒數切出音檔(0.025, 0.075).wav音值資料()
        self.assertEqual(wav音值資料, b'0' * 800 + b'1' * 800)

    def test_讀WAVE_FORMAT_EXTENSIBLE檔(self):
        聲音檔.對檔案讀(self.format65534所在)

    def test_讀別種檔案(self):
        with self.assertRaises(wave.Error):
            聲音檔.對資料轉(b'im.read()')
